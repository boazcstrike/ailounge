# `src/utils` Directory

This directory contains various utility scripts that provide helper functions for the AI Lounge application.

## Files

-   **`api.py`**: This script provides a function to send requests to a local Ollama API endpoint to generate chat responses from a specified model.

-   **`combine.py`**: This file appears to be a placeholder or a note from the developer.

-   **`coqui.py`**: This script uses the `TTS` (Coqui TTS) library to perform text-to-speech conversion. It can save the generated speech to a `.wav` file and play it.

-   **`main.py`**: This script contains general-purpose utility functions for file handling and text cleaning. It includes functions to read from a file, save content to a file with a timestamp, and parse text to remove special characters and formatting.

-   **`mread.py`**: This script reads a chat log from a file and uses the `pyttsx3` library to narrate the conversation, alternating between different voices for the speakers.

-   **`narrator.py`**: This script defines a `Narrator` class that can be used for text-to-speech. It supports both `pyttsx3` and `edge_tts` as TTS engines.

-   **`organize.py`**: This script is used to combine multiple text files from the `dump` directory into a single file.

-   **`ref.py`**: This script appears to be an older or alternative version of the main application logic. It sets up a conversation between two AI characters with predefined personalities and instructions, and it includes logic for managing context memory and saving the conversation history.

-   **`searcher.py`**: This script defines a `Searcher` class that can perform web searches using a SearxNG instance. It uses a language model to generate search queries from a given text, summarize the search results, and parse the content of web pages.
