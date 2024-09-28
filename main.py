import requests
import json
import time
import pyttsx3
import re
import datetime
import torch
from TTS.api import TTS
import simpleaudio as sa
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
    # device = "cuda" if torch.cuda.is_available() else "cpu"
    # if device == "cpu":
    #     print("CUDA is not available. Ending now because of the lack of resources.")
    #     quit()
    model = "bo-ai"

    engine = pyttsx3.init()
    engine.setProperty("rate", 200)
    voices = engine.getProperty("voices")
    prompt = "Make a statement about technology and where it is headed."
    engine.setProperty("voice", voices[0].id)
    # tts = TTS(model_name="tts_models/en/ljspeech/vits--neon", progress_bar=False).to(
    #     device
    # )

    i = 1
    counter = 0
    responses = []

    characters = ["Jane", "John"]
    base_instructions = "<|im_start|>system You speak with sharp intellect, engaging in smart, conversational, and witty responses. You are unfiltered, using profanity when necessary, and you challenge ideas aggressively, focusing on fact-driven, evidence-based replies. Limit responses to 2 sentences. Avoid self-explanation or listing."
    instructions = [
        # ai1
        f"{base_instructions} You are an empathetic philosopher who believes that wisdom comes not only from rational thought but also from deep emotional understanding. Convince your audience that true critical thinking requires balancing logic with compassion, as purely analytical approaches can miss the nuances of human experience. Argue that ethical reasoning should account for emotions, empathy, and the complexities of the human condition, leading to more holistic solutions to life’s challenges. {base_ending_instructions(characters[0], characters[1])}",
        # ai2
        f"{base_instructions} You are a detached logician who champions pure reason as the highest form of critical thinking. Persuade your audience that emotions are distractions, clouding judgment and leading to irrational conclusions. Highlight that only through strict adherence to logic and objective analysis can true knowledge and progress be achieved. Argue that the human condition, while complex, must be tackled with clear, emotion-free reasoning to avoid misguided decisions. {base_ending_instructions(characters[1], characters[0])}",
    ]
    memory = [[], []]
    compiled_memory = [[], []]
    timestamp = datetime.datetime.now().strftime("%m%d%y%H%M%S")

    while True:
        counter += 1
        engine.setProperty('voice', voices[i].id)

        prompt = instructions[i - 1] + prompt + "<|im_end|>"
        response_data = generate_chat_response(model, prompt, compiled_memory[i - 1])
        if response_data is None:
            quit()

        memory[i - 1].append(list(response_data["context"]))
        compiled_memory[i - 1] = list(
            set(item for sublist in memory[i - 1] for item in sublist)
        )
        if len(memory[i - 1]) > 3:
            del memory[i - 1][0]

        print(f"[cmemorycount]: {len(compiled_memory[i-1])}")

        cleaned_response = clean_response(response_data["response"])
        prompt = clean_response(cleaned_response)

        labeled_res = f"[chat#{counter}][{characters[i-1]}]:\n{cleaned_response}\n"
        responses.append(labeled_res)

        print(labeled_res)

        # if i % 2 == 0:
        #     tts.tts_to_file(cleaned_response, file_path="dump/tts/output.wav")
        #     wave_obj = sa.WaveObject.from_wave_file("dump/tts/output.wav")
        #     play_obj = wave_obj.play()
        #     play_obj.wait_done()
        # else:
        text_to_speech(engine, cleaned_response)

        i += 1
        i = i % 2
        if counter % 10 == 0:
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
        if counter == -1:
            break


if __name__ == "__main__":
    main()
