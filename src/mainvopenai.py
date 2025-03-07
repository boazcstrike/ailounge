import time
from datetime import datetime
import threading
from openai import OpenAI

from utils.main import save_file, parse_contents
from utils.searcher import Searcher
from constants import (
    instructions,
    final_mediator_prompt,
)
from termcolor import colored
from consciousness import self_reflect, rethink


def main():
    client = OpenAI(
        api_key=''
    )
    
    i = 0
    counter = 0
    timestamp = datetime.now().strftime("%m%d%y%H%M%S")

    characters = ["Jarvis", "Her"]
    messages = []
    conversation_history = []

    prompt = "Make a statement of what you believe in about startups focusing on psychology and mental health through technology and how we can leverage technology to improve our consciousness."
    timestamp = datetime.now().strftime("%m%d%y%H%M%S")
    
    try:
        while True:
            time.sleep(2)
            counter += 1
            i = counter % 2

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": str(instructions[i])},
                    {"role": "user", "content": prompt}
                ]
            ).choices[0].message.content.strip()
            response = parse_contents(response)

            labeled_res = f"\n[{datetime.now().strftime('%m.%d.%y %H:%M:%S.%f')[:-3]}][chat#{counter}][{characters[i]}]:\n{response}\n"
            print(colored(labeled_res, 'light_blue' if counter % 2 != 0 else 'light_green'))
            conversation_history.append(labeled_res)

            prompt = response

            if counter % 6 == 0:
                save_file_thread = threading.Thread(target=save_file, args=(conversation_history, timestamp))
                save_file_thread.start()
            if counter % 50 == 0:
                time.sleep(3)
                timestamp = datetime.now().strftime("%m%d%y%H%M%S")
                conversation_history = []
    except KeyboardInterrupt:
        print(colored("ending conversation...\n" , 'red'))
        print("\033[?25h", end="")
        return


if __name__ == "__main__":
    main()
