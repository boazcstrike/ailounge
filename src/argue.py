import time
from datetime import datetime
import threading
from langchain_ollama.llms import OllamaLLM
from langchain_core.messages import HumanMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import (
    PipelinePromptTemplate,
    PromptTemplate,
    ChatPromptTemplate,
)

from utils.main import save_file, parse_contents
from utils.searcher import Searcher
from constants.main import (
    instructions,
    final_mediator_prompt,
)
from termcolor import colored
from consciousness import self_reflect, rethink


def main():
    # ollama model to use
    model = OllamaLLM(
        # model="L3.2-8X3B-MOE-Dark-Champion-Inst-18.4B-uncen-ablit_D_AU-Q3_k_s",
        # temperature=1,
        # num_ctx=4096,
        # repeat_last_n=-1,
        # repeat_penalty=1.2,
        # top_k=80,
    )
    # searxng = Searcher(model)

    i = 0
    counter = 0
    timestamp = datetime.now().strftime("%m%d%y%H%M%S")

    # girl, boy usually, based on built-in windows tts
    characters = ["Jarvis", "Her"]
    # placeholder for the context of the prompt
    messages = []
    # # conversation history will be filled with the chat history with labels
    conversation_history = []
    # chat_history = [
    #     InMemoryChatMessageHistory(),
    #     InMemoryChatMessageHistory(),
    # ]
    # baseline instructions for both of them

    # * this is your prompt
    prompt = "Make a statement of what you believe in about startups focusing on psychology and mental health through technology and how we can leverage technology to improve our consciousness."
    timestamp = datetime.now().strftime("%m%d%y%H%M%S")
    # mediator_enabled = input("Do you want to enable the mediator? (y/n): ")
    try:
        while True:
            counter += 1
            i = counter % 2

            response = model.invoke(messages)
            response = parse_contents(response)

            response = rethink(model, prompt, response, instructions[i])

            labeled_res = f"\n[{datetime.now().strftime('%m.%d.%y %H:%M:%S.%f')[:-3]}][chat#{counter}][{characters[i]}]:\n{response}\n"
            print(colored(labeled_res, 'light_blue' if counter % 2 != 0 else 'light_green'))
            conversation_history.append(labeled_res)

            # print("conversation_history: ", conversation_history[:35], "...", conversation_history[-35:])

            # if mediator_enabled == "y":
            #     chain = final_mediator_prompt | model
            #     chat_to_score = conversation_history[counter-1] if counter <= 1 else conversation_history[counter-1] + "\n" + conversation_history[counter-2]
            #     score = chain.invoke({"input": chat_to_score})
            #     labeled_res = f"[{datetime.now().strftime('%m.%d.%y %H:%M:%S.%f')}][chat#{counter}][mediator]: {score}"
            #     print(colored(labeled_res, 'cyan'))
            #     conversation_history.append(labeled_res)

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
