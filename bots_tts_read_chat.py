import pyttsx3
import re


def text_to_speech(engine, text):
    engine.say(text)
    engine.runAndWait()


def read_file(file_path):
    with open(f"dump/{file_path}", "r") as file:
        content = file.read()
        chats = re.split(r"\[chat#\d+\]\[\w+\]:\n", content)
        chats = [chat for chat in chats]
    return chats


def main():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")

    counter = 0
    file_to_read = input("Enter the .txt file to read (sampleresponse.txt): ")
    while True:
        counter += 1
        i = counter % 2
        engine.setProperty("voice", voices[i].id)

        chats = read_file(file_to_read)
        cleaned_response = re.sub(r"\[chat#\d+\]AI\[\d+\]:", "", chats[counter]).strip()
        print(f"\n[chat#{counter}]: {cleaned_response}")
        text_to_speech(engine, cleaned_response)


if __name__ == "__main__":
    main()
