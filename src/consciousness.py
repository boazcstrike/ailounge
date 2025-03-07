from time import sleep

from termcolor import colored
from constants import reflection_prompt, think_prompt


def self_reflect(model, previous_response, current_answer, instructions, iterations=3):
    answer = current_answer
    for _ in range(iterations):
        print(f"[thinking...AHA!]\n{colored(answer, 'white')}")
        new_answer = model(reflection_prompt.format(
            previous_response=previous_response,
            current_answer=answer,
            instructions=instructions))
        if not new_answer:
            print("Model returned an empty response.")
        answer = new_answer
    return answer


def rethink(model, user_input, current_answer, instructions, iterations=3):
    answer = current_answer
    previous_bot_response = ""
    for _ in range(iterations):
        print(f"[thinking...AHA!]\n{colored(answer, 'white')}")
        sleep(0.4)
        new_answer = model.invoke(
            think_prompt.format(
                user_input=user_input,
                previous_bot_response=previous_bot_response,
                current_bot_response=answer,
                instructions=instructions,))
        if not new_answer:
            print("Model returned an empty response.")
        answer = new_answer
    return answer

