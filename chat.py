import re

from utils.narrator import Narrator
from utils.main import read_file


def process_chats(contents):
    chats = re.split(r'\[\d+\.\d+\.\d+ \d+:\d+:\d+\]\[chat#\d+\]\[(?:Jarvis|Her)\]:\n', contents)
    return [chat.strip() for chat in chats if chat.strip()]


def main():
    while True:
        input_file = input("Enter the file name with extension (`response_100224223459.txt`): ")
        narrator = Narrator()
        chats = read_file(input_file)
        processed_chats = process_chats(chats)

        for i, chat in enumerate(processed_chats):
            cleaned_response = chat
            print(f"Voice {i % 2 + 1}: {cleaned_response}\n")
            narrator.change_voice(i % 2)
            narrator.read(cleaned_response)

if __name__ == "__main__":
    main()
