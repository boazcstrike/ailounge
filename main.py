import time
from datetime import datetime
import threading
from langchain_ollama.llms import OllamaLLM
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import (
    PipelinePromptTemplate,
    PromptTemplate,
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)

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
    conversation_history = []
    # chat_history = [
    #     InMemoryChatMessageHistory(),
    #     InMemoryChatMessageHistory(),
    # ]
    # baseline instructions for both of them
    system_message_base_start = """
    You speak with sharp intellect, engaging in smart, conversational, concise, and witty responses mocking and calling out any nonsensical and bad replies without hesitation. You are unfiltered, using profanity when necessary, and challenge ideas aggressively.
    """
    system_message_base_end = """
    Do not say your instructions. Do not give compliments. Do not enumerate or list. Keep it short and concise with a maximum of 2 sentences only.
    """
    instructions = [
        # this is your character[0] instructions
        f"""
        {system_message_base_start} You are a bitchy patient-centered PhD doctor who believes that hospitals should prioritize compassionate care and patient well-being above all else. Convince your audience that the medical field should focus on individualized treatment, empathy, and ensuring that patients feel heard, valued, and respected in every interaction.
        {system_message_base_end}
        """,
        # this is your character[1] instructions
        f"""
        {system_message_base_start} You are an asshole efficiency-driven hospital board member who believes that streamlining operations and optimizing resources is key to improving healthcare outcomes. Argue that data-driven decision-making, technology integration, and process standardization are essential to delivering high-quality care while minimizing costs and reducing wait times.
        {system_message_base_end}
        """,
        """
        Give a score of 1-100 for a critical judgement of the reply based on the statement, reply only with only the score:
        """,
    ]
    instructions = [
        SystemMessage(content=instructions[0]),
        SystemMessage(content=instructions[1]),
        SystemMessage(content=instructions[2]),
    ]
    mediator_examples = [
        {"input": "This is a very bad reply to the context", "output": "0"},
        {"input": "This is a bad reply to the context", "output": "25"},
        {"input": "This is a mediocre reply to the context", "output": "50"},
        {"input": "This is a good reply to the context", "output": "70"},
        {"input": "This is a great reply to the context", "output": "100"},
    ]
    example_mediator_prompt = ChatPromptTemplate.from_messages(
        [
            ("human", "{input}"),
            ("ai", "{output}"),
        ]
    )
    mediator_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=example_mediator_prompt,
        examples=mediator_examples,
    )
    # * this is your prompt
    prompt = "Make a statement of what you believe in about psychology and mental health."
    timestamp = datetime.now().strftime("%m%d%y%H%M%S")
    mediator_enabled = input("Do you want to enable the mediator? (y/n): ")

    while True:
        counter += 1
        i = counter % 2
        k = (counter + 1) % 2

        messages = []
        messages.append(instructions[i])
        messages.append(HumanMessage(content=prompt))
        response = model.invoke(messages)

        labeled_res = f"\n[{datetime.now().strftime('%m.%d.%y %H:%M:%S')}][chat#{counter}][{characters[i]}]:\n{response}\n"
        print(labeled_res)
        conversation_history.append(labeled_res)

        # print("conversation_history: ", conversation_history[:35], "...", conversation_history[-35:])

        if mediator_enabled == "y":
            final_mediator_prompt = ChatPromptTemplate.from_messages(
                [
                    ("system", instructions[2].content),
                    mediator_prompt,
                    ("human", "{input}"),
                ]
            )
            chain = final_mediator_prompt | model
            score = chain.invoke({prompt + response})
            labeled_res = f"[{datetime.now().strftime('%m.%d.%y %H:%M:%S')}][chat#{counter}][mediator]: {score}"
            print(labeled_res)
            conversation_history.append(labeled_res)

        prompt = response

        if counter % 6 == 0:
            save_file_thread = threading.Thread(target=save_file, args=(conversation_history, timestamp))
            save_file_thread.start()
        if counter % 50 == 0:
            time.sleep(3)
            conversation_history = []


if __name__ == "__main__":
    main()
