# `text-models` Directory

This directory is intended to store the language models used by the AI Lounge application. The models listed in this directory are likely used by the Ollama instance that the application connects to.

## Models

The models listed in this directory seem to be a variety of open-source language models, including:

-   `bo-instruct`, `bo-main`, `bo-mini`, `boai`: These might be custom or fine-tuned models.
-   `Deepthink-Reasoning-7B-Q8_0`
-   `L3.2-8X3B-MOE-Dark-Champion-Inst-18.4B-uncen-ablit_D_AU-Q3_k_s`
-   `Llama-3.2-4X3B-MOE-Ultra-Instruct-10B-D_AU-Q6_k`
-   `llama3.1-instruct-steroids`
-   `llama3.1-instruct-weakened`
-   `Phi-3.1-mini-128k-instruct-Q6_K_L`
-   `Phi-3.1-mini-128k-instruct-Q8_0`
-   `Phi-3.5-3.8B-vision-instruct-Q8_0`
-   `QW-6X1.5B-DeepSeek-Qwen-LAM-e32-Q4_K_S`
-   `recipe-ingredient-mistral-7b copy.Q4_K_M`
-   `Tess-v2.5-Phi-3-medium-128k-14B.i1-Q4_K_S`

## Usage

These models are likely loaded into Ollama and then specified in the agent configurations (e.g., in `src/agentsreader.py`) to be used by the AI agents.

## Note

The model files themselves are not included in this repository. To use the application, you will need to download and install the desired models for your Ollama instance. You can find many of these models on platforms like Hugging Face.
