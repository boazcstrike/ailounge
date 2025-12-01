# `src/constants` Directory

This directory stores the constant variables used throughout the AI Lounge application, particularly the prompts and messages that define the behavior and personality of the AI agents.

## `main.py`

This file contains the following key constants:

-   **`system_message_base_start` and `system_message_base_end`**: These multiline strings define the base instructions for the AI agents, setting their tone and personality as sharp, incisive, and critical thinkers.

-   **`instructions`**: A list of `SystemMessage` objects that contain the specific instructions for each agent role (e.g., the "researcher" and the "critic") and the "mediator". These instructions guide the agents' behavior during the debate and resolution phases.

-   **`mediator_examples`**: A list of examples used for few-shot prompting the mediator agent. These examples help the mediator learn how to score the responses and provide a joke.

-   **`example_mediator_prompt` and `mediator_prompt`**: These are `ChatPromptTemplate` and `FewShotChatMessagePromptTemplate` objects that structure the prompts for the mediator agent.

-   **`final_mediator_prompt`**: The final chat prompt template for the mediator, which includes the system message, the few-shot examples, and the user input.

-   **`reflection_prompt` and `think_prompt`**: These are `PromptTemplate` objects designed for the agents to reflect on their responses and improve them.
