import re

from narrator import Narrator
from main import read_file


def process_chats(contents):
    chats = re.split(r"\[chat#\d+\]\[\w+\]:\n", contents)
    chats = [chat for chat in chats]
    return chats


def main():
    narrator = Narrator()
    counter = 0
    file_to_read = input("Enter the `x.txt` file to read from dump with extension (sampleresponse.txt): ")
    chats = read_file(file_to_read)
    while True:
        counter += 1
        i = counter % 2
        chats = process_chats(chats)

        cleaned_response = re.sub(r"\[chat#\d+\]AI\[\d+\]:", "", chats[counter]).strip()
        print(f"AI[{i}]: {cleaned_response}")
        narrator.change_voice(i)
        narrator.read(cleaned_response)


if __name__ == "__main__":
    main()
