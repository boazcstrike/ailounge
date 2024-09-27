import pyttsx3
import re


# env\scripts\activate
def text_to_speech(engine, text):
    engine.say(text)
    engine.runAndWait()


def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        chats = re.split(r"(\[chat#\d+\]AI\[\d+\]:)", content)
        chats = [chat for chat in chats if chat.strip()]

        paired_chats = [chats[i] + chats[i + 1] for i in range(0, len(chats) - 1, 2)]
    return paired_chats


def main():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    prompt = "What is a good business that can generate revenue in the next years using technology and is related to pharmacy?"
    text_to_speech(engine, prompt)
    engine.setProperty("voice", voices[0].id)

    i = 0
    counter = 0
    bigcounter = 1

    while True:

        i = i % 2
        if i % 2 == 0:
            engine.setProperty("voice", voices[0].id)
        else:
            engine.setProperty("voice", voices[1].id)

        if bigcounter == 1:
            paired_chats = read_file(f"dump/response_business_opp1_{bigcounter}.txt")
        if counter % 10 == 0:
            bigcounter += 1
            paired_chats = read_file(f"dump/response_business_opp1_{bigcounter}.txt")
        chat_response = paired_chats[counter % len(paired_chats)]

        print(f"Processing chat {counter}: {chat_response}")
        cleaned_response = re.sub(r"\[chat#\d+\]AI\[\d+\]:", "", chat_response).strip()
        text_to_speech(engine, cleaned_response)

        i += 1
        counter += 1
        if counter == 243:
            break


if __name__ == "__main__":
    main()
