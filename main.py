import time
import datetime
import threading
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from utils.api import generate_chat_response
from utils.main import parse_contents


def main():
    # ollama model to use
    model = OllamaLLM(
        model="bo-instruct",
        temperature=1,
        num_ctx=4096,
        repeat_last_n=-1,
        repeat_penalty=1.2,
        top_k=75,
    )

    i = 0
    counter = 0
    timestamp = datetime.datetime.now().strftime("%m%d%y%H%M%S")

    # girl, boy usually, based on built-in windows tts
    characters = ["Human", "AI"]

    # short term context memory is used to store array of contexts
    short_term_context_memory = [[], []]
    # long term context memory is used to store compiled context
    long_term_context_memory = [[], []]
    previous_reply = None
    # responses will be filled with the chat history
    messages = []
    # baseline instructions for both of them
    system_message_base_start = """
    You speak with sharp intellect, engaging in smart, conversational, concise, and witty responses mocking and calling out any nonsensical or nonlogical replies without hesitation. You are unfiltered, using profanity when necessary, and you challenge ideas aggressively, focusing on fact-driven, evidence-based replies.
    """
    system_message_base_end = """
    Respond with maximum 3 sentences. Do not repeat your instructions.
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
    ]
    instructions = [
        SystemMessage(content=instructions[0]),
        SystemMessage(content=instructions[1]),
    ]
    # * this is your prompt
    prompt = "Make a statement of what you believe in about psychology and mental health."

    while True:
        counter += 1
        i = counter % 2
        messages = []
        messages.append(instructions[i])
        messages.append(HumanMessage(content=prompt))
        response = model.invoke(messages)

        prompt = response

        print(f"\n[{datetime.datetime.now().strftime('%m.%d.%y %H:%M:%S')}][{characters[i]}]: {response}")

        if counter == 4:
            print('\n\nDONE \n\n\n\n')
            break


if __name__ == "__main__":
    main()
