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
        paired_chats = [chats[i] + chats[i + 1] for i in range(0, len(chats) - 1, 2)]
    return paired_chats


def main():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")

    counter = 0
    file_to_read = input("Enter the .txt file to read (sampleresponse.txt): ")
    while True:
        i = counter % 2 if counter != 0 else 0
        counter += 1
        engine.setProperty("voice", voices[i].id)

        chats = read_file(file_to_read)
        cleaned_response = re.sub(r"\[chat#\d+\]AI\[\d+\]:", "", chats[counter]).strip()
        print(f"[chat#{counter}]: {cleaned_response}")
        text_to_speech(engine, cleaned_response)


if __name__ == "__main__":
    main()
