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


def open_ai_rethink(client, user_input, current_answer, instructions, iterations=2):
    answer = current_answer
    previous_bot_response = ""
    for _ in range(iterations):
        print(f"\n[thinking...AHA!]\n{colored(answer, 'white')}")
        sleep(0.4)
        new_answer = model.chat.completions.create(
            model="o3-mini",
            messages: [
                "role": "user",
                "content": f"""
                    User Input: {user_input}
                    Previous AI Response (if none, then first): {previous_bot_response}
                    Current AI Response: {current_bot_response}
                    Instructions: {instructions}

                    Absorb and Reflect:
                    - Analyze the current bot response in the context of the user input and previous bot response.
                    - Identify areas for improvement or clarification.
                    - Suggest enhancements for coherence and depth.
                    - Ensure alignment with the overall conversation flow.
                    - Adjust to instructions

                    Refined Bot Response:
                    """
            ])
        if not new_answer:
            print("Model returned an empty response.\n")
        answer = new_answer
    return answer

