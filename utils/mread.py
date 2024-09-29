import pyttsx3
import re
import time
import shutil


def text_to_speech(engine, text):
    engine.say(text)
    engine.runAndWait()


def main():
  engine = pyttsx3.init()
  engine.setProperty("rate", 200)
  voices = engine.getProperty("voices")
  characters = ["Jane", "John"]
  chats = []
  pattern = r'\[chat#\d+\]\[(\w+)\]:\s*([\s\S]*?)(?=\n\[chat#\d+\]|\Z)'
  counter = 0
  file_path = input("dump/filename?\n")
  while True:
    counter += 1
    i = counter % 2
    src = f'dump/{file_path}'
    dst = f'dump/{file_path}_read'
    shutil.copy(src, dst)

    if counter == 0 or counter % 10 == 0:
      with open(f"dump/{file_path}_read", "r") as file:
        # content = file.read()
        # chats = re.split(r"(\[chat#\d+\]\[\d+\]:)", content)
        for line in file:
          if line.startswith("[chat#"):
              message = line.split(']', 2)[2].strip()
              chats.append(message)
        print(chats)
      time.sleep(2)

    if len(chats) - counter < 3:
      print("chats are almost on the read counter")
      print("waiting 2 seconds...")
      time.sleep(2)
      continue

    cleaned_response = chats[counter]
    engine.setProperty('voice', voices[i].id)
    print(f"{characters[i]}: {cleaned_response}")
    text_to_speech(engine, cleaned_response)


if __name__ == "__main__":
  main()

