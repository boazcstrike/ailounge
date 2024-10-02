import re

from utils.narrator import Narrator
from utils.main import read_file


def process_chats(contents):
    chats = re.split(r'\[\d+\.\d+\.\d+ \d+:\d+:\d+\]\[chat#\d+\]\[(?:Human|AI)\]:\n', contents)
    return [chat.strip() for chat in chats if chat.strip()]


def main():
    narrator = Narrator()
    chats = read_file("response_100224213515.txt")
    processed_chats = process_chats(chats)

    for i, chat in enumerate(processed_chats):
        cleaned_response = chat
        print(f"Voice {i % 2 + 1}: {cleaned_response}\n")
        narrator.change_voice(i % 2)
        narrator.read(cleaned_response)

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
