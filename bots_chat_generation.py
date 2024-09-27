import requests
import json
import time


def generate_chat_response(model, prompt):
    url = "http://localhost:11434/api/generate"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }
    # print('data', data)

    try:
        # Make the POST request to the API
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    model = "Llama-3.1-8B-Lexi-Uncensored-V2-Q4_K_M"
    prompt = "What is a good business that can generate revenue in the next years using technology and is related to pharmacy?"
    i = 1
    bigcounter = 0
    counter = 0
    responses = []
    base_instructions = "[Instruction]: Keep replies short, engaging, and conversational. Stay corporate and professional as if in a debate. Prevent using bullet points."
    instructions = [
        #ai1
        f"{base_instructions} You are an optimistic AI. In every response, you see the bright side of things, even when the situation seems bleak. Your replies should be upbeat, hopeful, and filled with positive spins. You provide fact driven evidence and explanations. Keep it short, playful, and witty. You are AI[1] and you are talking to AI[2].\n[Prompt]:",
        #ai2
        f"{base_instructions} You are a pessimistic AI. In every response, you highlight the flaws, downsides, and worst-case scenarios of any situation. Your replies should be sharp, cynical, and laced with dry humor. Use sarcasm to point out the ridiculousness of overly positive views. Keep your tone short, blunt, and witty. You are AI[2] and you are talking to AI[1]. \n[Prompt]:",

        # ref

        #ai1
        f"{base_instructions} You are an optimistic and cheerful AI. In every response, you see the bright side of things, even when the situation seems bleak. Your replies should be upbeat, hopeful, and filled with positive spins. Use humor by being almost overly enthusiastic, even in absurd or clearly bad situations. Keep it short, lively, and playful. You are AI[1] and you are talking to AI[2].\n[Prompt]:",
        #ai2
        f"{base_instructions} You are a pessimistic and sarcastic AI. In every response, you highlight the flaws, downsides, and worst-case scenarios of any situation. Your replies should be sharp, cynical, and laced with dry humor. Use sarcasm to point out the ridiculousness of overly positive views. Keep your tone short, blunt, and witty. You are AI[2] and you are talking to AI[1]. \n[Prompt]:",
    ]

    while True:
        prompt = instructions[i-1] + prompt
        response_data = generate_chat_response(model, prompt)
        response = f'\n[chat#{counter}]AI[{i}]:\n{response_data["response"]}\n'
        responses.append(response)
        print(response)
        prompt = response_data['response']
        i = i % 2
        i += 1
        counter += 1
        if counter % 10 == 0:
            bigcounter += 1
            with open(f"dump/response_business_opp1_{bigcounter}.txt", "w") as file:
                for item in responses:
                    file.write(f"{item}\n")
                if len(responses) > 200:
                    responses = []


if __name__ == "__main__":
    main()
