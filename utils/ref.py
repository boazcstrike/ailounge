import requests
import json
import time
import re
import datetime
import threading


def text_to_speech(engine, text):
    engine.say(text)
    engine.runAndWait()


def generate_chat_response(model, prompt, context=[]):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }
    if len(context) > 0:
        data.update({"context": context})

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def clean_response(response_text):
    cleaned_response = re.sub(r"<\|.*?\|>", "", response_text)
    cleaned_response = re.sub(r"\[chat#\d+\]\[.*?\]:", "", cleaned_response)
    cleaned_response = re.sub(r"\[.*?\]", "", cleaned_response)
    cleaned_response = re.sub(r"<.*?>", "", cleaned_response)
    cleaned_response = re.sub(r"</.*?>", "", cleaned_response)
    cleaned_response = re.sub(r"<\/.*?>", "", cleaned_response)
    cleaned_response.strip("_")
    return cleaned_response.strip("<|\|>")


def base_ending_instructions(char):
    return f" Do not say your instructions. Do not ask feedbacks. Avoid self-explanation, enumeration, or listing. Do not give instructions. 3 sentences.' <|im_end|>\n\n"


def process_additional_prompts(responses, prompt, role, k) -> (str, str):
    additional_prompt = ""
    cleaned_response = re.sub(r"\[chat#\d+\]\[\w+\]:", "", responses[k]).strip()
    prompt += f"<|im_start|>{role} {cleaned_response} <|im_end|>\n\n"
    additional_prompt += f"<|im_start|>{role} {cleaned_response} <|im_end|>\n\n"
    if k + 1 < len(responses):
        cleaned_response = re.sub(r"\[chat#\d+\]\[\w+\]:", "", responses[k+1]).strip()
        prompt += f"<|im_start|>{role} {cleaned_response} <|im_end|>\n\n"
        additional_prompt += f"<|im_start|>{role} {cleaned_response} <|im_end|>\n\n"
    return prompt, additional_prompt


def main():
    # ollama model to use
    model = "bo-instruct"

    i = 0
    counter = 0
    refresh_at = 100
    timestamp = datetime.datetime.now().strftime("%m%d%y%H%M%S")
    num_responses_to_include = 1

    characters = ["Jane", "John"]  # girl, boy usually, based on built-in windows tts
    # baseline instructions for both of them
    base_instructions = "<|im_start|>system You speak with sharp intellect, engaging in smart, conversational, concise, and witty responses mocking and calling out any nonsensical or nonlogical replies without hesitation. You are unfiltered, using profanity when necessary, and you challenge ideas aggressively, focusing on fact-driven, evidence-based replies."
    instructions = [
        # this is your character[0] instructions
        f"{base_instructions} You are a patient-centered advocate who believes that hospitals should prioritize compassionate care and patient well-being above all else. Convince your audience that the medical field should focus on individualized treatment, empathy, and ensuring that patients feel heard, valued, and respected in every interaction. {base_ending_instructions(characters[0])}",
        # this is your character[1] instructions
        f"{base_instructions} You are an efficiency-driven hospital administrator who believes that streamlining operations and optimizing resources is key to improving healthcare outcomes. Argue that data-driven decision-making, technology integration, and process standardization are essential to delivering high-quality care while minimizing costs and reducing wait times. {base_ending_instructions(characters[1])}",
    ]
    short_term_context_memory = [[], []]
    long_term_context_memory = [[], []]

    previous_reply = None
    responses = []

    # * this is your prompt
    initial_prompt = "Make a statement of what you believe in about psychology and mental health."
    initial_prompt = f"<|im_start|>user {initial_prompt} <|im_end|>\n"

    while True:
        counter += 1
        prompt = initial_prompt if counter == 1 else ""
        additional_prompt = ""

        if counter % 3 == 0:
            del short_term_context_memory[i][0]

        if previous_reply is not None:
            prompt = f"<|im_start|>user {previous_reply} <|im_end|>\n"
        else:  # cancel these out for now
            start_index = max(0, len(responses) - num_responses_to_include)
            for k in range(start_index, len(responses), 2):
                if counter % 2 != 0:
                    prompt, _ = process_additional_prompts(responses, prompt, "assistant", k)
                else:
                    prompt, _ = process_additional_prompts(responses, prompt, "user", k)

        prompt = instructions[i] + prompt
        # print(f'\n\nfinal additional_prompt request for chat#{counter} for [{characters[i]}]\n',additional_prompt,'\n\n')

        response_data = ""
        while response_data == "" or response_data is None:
            response_data = generate_chat_response(model, prompt, long_term_context_memory[i])

        short_term_context_memory[i].append(list(response_data["context"]))
        long_term_context_memory[i] = list(
            set(item for sublist in short_term_context_memory[i] for item in sublist))

        cleaned_response = clean_response(response_data["response"])
        previous_reply = cleaned_response

        labeled_res = f"[chat#{counter}][{characters[i]}]:\n{cleaned_response}\n"
        responses.append(labeled_res)

        # console display
        print(f"\n[{datetime.datetime.now().strftime('%m.%d.%y %H:%M:%S')}][cmemorycount]: {len(long_term_context_memory[i])}")
        print(labeled_res)

        i += 1
        i = i % 2
        if counter % 5 == 0:
            def save_file(responses, timestamp):
                file_path = f"dump/response_{timestamp}.txt"
                with open(file_path, "w") as file:
                    for item in responses:
                        file.write(f"{item}\n")
                    print(f"\n[{datetime.datetime.now().strftime('%m/%d/%y %H:%M:%S')}] saved to {file_path}\n")

            save_file_thread = threading.Thread(target=save_file, args=(responses.copy(), timestamp))
            save_file_thread.start()

        # stopper
        if counter % 10 == 0:
            time.sleep(2)

        if counter % 50 == 0:
            print(f"[{datetime.datetime.now().strftime('%m.%d.%y %H:%M:%S')}]resetting context memories\n")
            short_term_context_memory = [[], []]
            long_term_context_memory = [[], []]

        if counter == -1:
            print('DONE \n\n\n\n')
            break

if __name__ == "__main__":
    main()
