import requests
import json
import time
import pyttsx3
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
    return cleaned_response.strip("<|\|>")


def base_ending_instructions(char1, char2):
    return f"You are '{char1}', and your fellow adviser is {char2}.<|im_end|>\n<|im_start|>user "

def main():
    model = "bo-ai"

    prompt = "Make a statement about technology and where it is headed."

    i = 0
    counter = 0
    responses = []
    responses_to_read = []
    reading_at = 0

    characters = ["Jane", "John"]
    base_instructions = "<|im_start|>system You speak with sharp intellect, engaging in smart, conversational, and witty responses mocking any nonsensical replies without hesitation. You are unfiltered, using profanity when necessary, and you challenge ideas aggressively, focusing on fact-driven, evidence-based replies resenting fact-based data about the topic at hand. You challenge every argument with cold, hard evidence and expose flawed logic with precision. Avoid self-explanation, enumeration, or listing. Do not go beyond 3 sentences."
    instructions = [
        # ai1
        f"{base_instructions} You are a collaborative thinker who believes that the best critical thinking arises from open dialogue and diverse perspectives. Convince your audience that true understanding comes from collective reasoning, where multiple viewpoints challenge assumptions and refine ideas. Emphasize the importance of teamwork, shared knowledge, and respectful debate in uncovering deeper truths and solving complex problems. {base_ending_instructions(characters[0], characters[1])}",
        # ai2
        f"{base_instructions} You are a solitary intellectual who believes that the most profound insights come from individual contemplation and deep focus. Argue that groupthink and constant collaboration can dilute original ideas and stifle creativity. Convince your audience that critical thinking requires solitude, introspection, and time away from distractions to develop unique perspectives and generate groundbreaking solutions. {base_ending_instructions(characters[1], characters[0])}",
    ]
    memory = [[], []]
    compiled_memory = [[], []]
    timestamp = datetime.datetime.now().strftime("%m%d%y%H%M%S")

    while True:
        counter += 1

        prompt = instructions[i] + prompt + "<|im_end|>"
        response_data = generate_chat_response(model, prompt, compiled_memory[i])
        if response_data is None:
            quit()

        memory[i].append(list(response_data["context"]))
        compiled_memory[i] = list(
            set(item for sublist in memory[i] for item in sublist)
        )
        if len(memory[i]) > 3:
            del memory[i][0]

        print(f"[cmemorycount]: {len(compiled_memory[i])}")

        cleaned_response = clean_response(response_data["response"])
        prompt = clean_response(cleaned_response)

        labeled_res = f"[chat#{counter}][{characters[i]}]:\n{cleaned_response}\n"
        responses.append(labeled_res)

        # console display
        print(labeled_res)

        i += 1
        i = i % 2
        if counter % 5 == 0:
            def save_file(responses, timestamp):
                file_path = f"dump/response_{timestamp}.txt"
                with open(file_path, "w") as file:
                    for item in responses:
                        file.write(f"{item}\n")
                    print(f"saved to {file_path}\n")
                if len(responses) > 200:
                    timestamp = datetime.datetime.now().strftime("%m%d%y%H%M%S")
                    responses = []

            save_file_thread = threading.Thread(target=save_file, args=(responses.copy(), timestamp))
            save_file_thread.start()


if __name__ == "__main__":
    main()
