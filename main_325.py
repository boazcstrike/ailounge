class OllamaAI:
    def __init__(self, name):
        self.name = name
        self.history = []

    def send_message(self, message):
        self.history.append(f"You: {message}")
        response = self.generate_response(message)
        self.history.append(f"{self.name}: {response}")
        return response

    def generate_response(self, message):
        # Simulate AI response generation
        return f"Response to '{message}'"

    def get_history(self):
        return "\n".join(self.history)

def main():
    ai1 = OllamaAI("AI_1")
    ai2 = OllamaAI("AI_2")

    conversation_turns = 5
    message = "Hello"

    for _ in range(conversation_turns):
        response1 = ai1.send_message(message)
        time.sleep(1)  # Simulate processing time
        response2 = ai2.send_message(response1)
        time.sleep(1)  # Simulate processing time
        message = response2

    print("AI_1 Conversation History:")
    print(ai1.get_history())
    print("\nAI_2 Conversation History:")
    print(ai2.get_history())
    