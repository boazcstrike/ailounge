# AI Lounge Project Overview

This project, "AI Lounge," is a sophisticated multi-agent AI system designed to provide comprehensive answers to user questions. It operates on a "research -> debate -> resolve -> present" workflow, leveraging a team of specialized AI agents. The system is built using the `agno` library, which facilitates agent creation, model integration (supporting `Ollama` and `OpenAIChat`), and tool utilization (including `DuckDuckGoTools`, `NewspaperTools`, and `FileTools`).

## Project Structure and Key Components

- **`src/agentsteam.py`**: This is the main entry point and orchestrator of the multi-agent system. It defines and instantiates the `Journalist`, `Researcher`, `Writer`, and `Reporter` agents, setting their roles, instructions, and the models they use.
- **`src/agentsreader.py`**: This file contains utility functions primarily for post-processing agent outputs. It includes `clean_md_to_script` for converting Markdown text into a conversational script format and integrates with text-to-speech functionalities.
- **`src/prompts/list.txt`**: This file stores a collection of diverse and complex topics/prompts that the AI agents can process. It serves as a repository for guiding the agents' research and response generation.
- **`.env`**: Used for securely storing API keys, such as `OPENAI_API_KEY`, which are loaded at runtime.
- **`src/tmp/`**: This directory is used for saving intermediate and final outputs of the agent interactions, including lists of URLs and research reports.

## Building and Running the Application

### Prerequisites

- Python 3.x
- `pip` package manager

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/ailounge.git
    cd ailounge
    ```
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up API Keys**: Create a `.env` file in the project root and add your OpenAI API key:
    ```
    OPENAI_API_KEY="your_openai_api_key_here"
    ```

### Running the System

To execute the AI Lounge system with a specific question, run the `agentsteam.py` script from the project root:

```bash
python -m src.agentsteam "What is the future of AI?"
```
The system will initiate the multi-agent workflow, and the final answer will be printed to the console.

## Development Conventions

-   **Agent Configuration**: Agents are configured and instantiated within `src/agentsteam.py`, where their roles, instructions, and the models they utilize are defined.
-   **Prompt Customization**: The prompts and topics that guide the agents' behavior can be modified or extended in `src/prompts/list.txt`.
-   **Output Processing**: Markdown outputs from agents are processed and cleaned using utilities in `src/agentsreader.py`, which also integrates with text-to-speech for audible responses.
-   **API Key Management**: Sensitive API keys are managed via environment variables loaded from a `.env` file.
