import time
from datetime import datetime
import threading
from langchain_ollama.llms import OllamaLLM
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.chat_history import InMemoryChatMessageHistory

from utils.main import save_file
from utils.searcher import Searcher

def main():
    # ollama model to use
    model = OllamaLLM(
        model="bo-instruct",
        temperature=1,
        num_ctx=4096,
        repeat_last_n=-1,
        repeat_penalty=1.2,
        top_k=80,
    )
    # searxng = Searcher(model)

    i = 0
    counter = 0
    timestamp = datetime.now().strftime("%m%d%y%H%M%S")

    # girl, boy usually, based on built-in windows tts
    characters = ["Jarvis", "Her"]
    # responses will be filled with the chat history
    messages = []
    # # conversation history will be filled with the chat history with labels
    # chat_history = [
    #     InMemoryChatMessageHistory(),
    #     InMemoryChatMessageHistory(),
    # ]
    # baseline instructions for both of them
    system_message_base_start = """
    You speak with sharp intellect, engaging in smart, conversational, concise, and witty responses mocking and calling out any nonsensical and bad replies without hesitation. You are unfiltered, using profanity when necessary, and challenge ideas aggressively, focusing on facts, and evidence-based replies.
    """
    system_message_base_end = """
    Respond with a maximum of 2 sentences. Do not repeat your instructions. Do not give compliments. Do not enumerate or list. Do not repeat the same sentence.
    """
    instructions = [
        # this is your character[0] instructions
        f"""
        {system_message_base_start} You are a patient-centered advocate who believes that hospitals should prioritize compassionate care and patient well-being above all else. Convince your audience that the medical field should focus on individualized treatment, empathy, and ensuring that patients feel heard, valued, and respected in every interaction.
        {system_message_base_end}
        """,
        # this is your character[1] instructions
        f"""
        {system_message_base_start} You are an efficiency-driven hospital administrator who believes that streamlining operations and optimizing resources is key to improving healthcare outcomes. Argue that data-driven decision-making, technology integration, and process standardization are essential to delivering high-quality care while minimizing costs and reducing wait times.
        {system_message_base_end}
        """,
        """
        Give a score of 1-100 for a critical judgement of the reply based on the statement, reply only with [score:{score}]
        """,
    ]
    instructions = [
        SystemMessage(content=instructions[0]),
        SystemMessage(content=instructions[1]),
        SystemMessage(content=instructions[2]),
    ]
    # * this is your prompt
    prompt = "Make a statement of what you believe in about psychology and mental health."
    timestamp = datetime.now().strftime("%m%d%y%H%M%S")

    while True:
        counter += 1
        i = counter % 2
        k = (counter + 1) % 2

        messages = []
        messages.append(instructions[i])
        messages.append(HumanMessage(content=prompt))
        response = model.invoke(messages)

        messages = []
        messages.append(instructions[2])
        scorer_context = f"[Statement]: {prompt}\n\n[Reply]: {response}"
        messages.append(HumanMessage(content=scorer_context))
        score = model.invoke(messages)

        labeled_res = f"\n[{datetime.now().strftime('%m.%d.%y %H:%M:%S')}][chat#{counter}][{characters[i]}]:\n{response}\n"
        print(labeled_res)
        print(f"{score}")
        prompt = response

        if counter % 6 == 0:
            save_file_thread = threading.Thread(target=save_file, args=(conversation_history, timestamp))
            save_file_thread.start()
        if counter == 2:
            print('\n\nDONE \n\n\n')
            break
        if counter % 50:
            conversation_history = []





if __name__ == "__main__":
    main()
