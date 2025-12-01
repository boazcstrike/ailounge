# AI Lounge

AI Lounge is a multi-agent AI system where a team of AI agents collaborates to provide comprehensive answers to user questions. The system follows a "research -> debate -> resolve -> present" workflow to generate well-rounded and nuanced responses.

This repository contains everything about AI and testing it in one personal workspace.

## Features

- **Multi-Agent System:** Utilizes a team of AI agents with different roles (e.g., researcher, critic, resolver) to tackle complex questions.
- **Collaborative Workflow:** Agents work together in a structured workflow to research, debate, and synthesize information.
- **Customizable Agents:** Agent configurations can be defined and customized in `src/agentsreader.py`.
- **Extensible Prompts:** The prompts used by the agents can be modified in `src/prompts/list.txt`.
- **Text-to-Speech (TTS):** The final answer can be converted to speech using the `pyttsx3` library.

## Workflow

The AI Lounge system follows a four-step workflow:

1.  **Research:** The "researcher" agent gathers information to answer the user's question.
2.  **Debate:** The "critic" agent challenges the researcher's findings, and the two agents debate to refine the answer.
3.  **Resolve:** The "resolver" agent steps in to synthesize the arguments and generate a final, consolidated answer.
4.  **Present:** The final answer is presented to the user in a structured JSON format.

## Getting Started

### Prerequisites

- Python 3.x
- `pip` package manager

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/ailounge.git
    cd ailounge
    ```

2.  Install the required dependencies from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To run the AI Lounge system, execute the `agentsteam.py` script from the root directory with a question as an argument:

```bash
python -m src.agentsteam "What is the future of AI?"
```

The system will then initiate the multi-agent workflow, and the final answer will be printed to the console.

## Configuration

The AI agents can be configured in the `src/agentsreader.py` file. This file defines the roles, prompts, and models used by each agent in the team.

## Prompts

The prompts that guide the behavior of the AI agents are stored in `src/prompts/list.txt`. You can modify these prompts to customize the agents' responses and personalities.

## Text-to-Speech (TTS)

The `argue_tts.py` script provides a text-to-speech functionality to read the generated answer aloud. To use this feature, you may need to install additional system-level TTS engines.



## All in one

[Harbor](https://github.com/av/harbor)
Containerized LLM toolkit. Run LLM backends, APIs, frontends, and additional services via a concise CLI.

## Prompt Libraries

- [AI LLM System Prompts Gsheet](https://docs.google.com/spreadsheets/d/1lk6JNKtl3D4bx9b5z_kJ5J8UqMYj0WKFdQ2yE7R87kg/edit?gid=0#gid=0)
- [msty prompt library](https://msty.app/prompts-library)
- [aiforedu](https://www.aiforeducation.io/prompt-library)
- [hammerai](https://www.hammerai.com/)

## LLM Leaderboards

[AI Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)

###### My PC Setup

```
i5 6600K 4-cores
GTX 1070 8gbvram
16gb RAM
```


## LLMs

*all more than 6.8gb pushes to CPU if higher settings*

###### mistral-nemo
* mistral-nemo:12b-instruct-2407-q4_0 8.1gb - bad
* mistral-nemo:12b-instruct-2407-q3_K_M 7.6gb - good, slight throttle with non-default
- earlier knowledge cutoff and conversational

###### llama3.1
* llama3.1:8b-instruct-q3_K_S - good; low quality
* llama3.1:8b-instruct-q5_1 - best so far
* llama3.1:8b-instruct-q6_K - good: nothing running, throttle with non-default
- recommended: 8 cores, 16gm ram, 3000 series GPU
- up to date knowledge cutoff and conversational

###### gemma2
* gemma2:9b-instruct-q4_1 - ok: nothing running, throttle on non-default
* gemma2:9b-instruct-q5_1 - a little slow
* gemma2:9b-instruct-q6_K - slow, default settings ok throttling
- recommended: none, modelfile below GPU VRAM
- reasoning and coding tasks

###### deepseekcoderv2
- recommended: modelfile solo run
- reasoning and coding tasks

###### phi3:latest - fast
- recommended: lowest

### LLM Chat Web UI Platforms
- [Mysty](https://msty.app/) ⭐️⭐️⭐️⭐️⭐️
- [gemma2 recommended](https://github.com/ivanfioravanti/chatbot-ollama ) ?
- [mobile app](https://github.com/AugustDev/enchanted) ⭐️⭐️⭐️⭐️⭐️

## TTS

tutorials:
- [Piper training tutorial](https://ssamjh.nz/create-custom-piper-tts-voice/)

repos:
- [AlwaysReddy](https://github.com/ILikeAI/AlwaysReddy)
- [Piper](https://github.com/rhasspy/piper)
- [High-performance inference of OpenAI's Whisper automatic speech recognition (ASR) model](https://github.com/ggerganov/whisper.cpp)
- [XTTS-2-UI](https://github.com/BoltzmannEntropy/xtts2-ui)
- [ttispiper](https://github.com/voicedock/ttspiper)
dockerized piper
```
docker run --rm -v "$(pwd)/config:/data/config" -v "$(pwd)/dataset:/data/dataset" -p 9999:9999 ghcr.io/voicedock/ttspiper:latest ttspiper
```


## random later repos:

https://github.com/danwiseman/epimetheus
https://github.com/hybridx/ai-slack-companion
https://github.com/Fortyseven/ircawp
[fabric](https://github.com/danielmiessler/fabric) is an open-source framework for augmenting humans using AI.

[slack bot](https://github.com/village0/slack_bot)

[Dify](https://github.com/langgenius/dify) is an open-source LLM app development platform. Its intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. Here's a list of the core features:


[Jina](https://github.com/jina-ai/jina) lets you build multimodal AI services and pipelines that communicate via gRPC, HTTP and WebSockets, then scale them up and deploy to production. You can focus on your logic and algorithms, without worrying about the infrastructure complexity.


[MemFree](https://github.com/memfreeme/memfree) is a hybrid AI search engine that simultaneously performs searches on your personal knowledge base (such as bookmarks, notes, documents, etc.) and the Internet.

[MindsDB](https://github.com/mindsdb/mindsdb)
MindsDB is the platform for customizing AI from enterprise data. You can create, serve, and fine-tune models in real-time from your database, vector store, and application data.

## references

[llm caching fastapi](https://medium.com/@chinmayd49/self-host-llm-with-ec2-vllm-langchain-fastapi-llm-cache-and-huggingface-model-7a2efa2dcdab#:~:text=I%20would%20recommend%20go%20through,for%20ML%20and%20LLM%20specifically.&text=For%20application%20and%20OS%20images,softwares%20and%20are%20command%20friendly.)

- https://topai.tools/t/automatic-1111
- https://zrok.io/pricing/
- https://localhost.run/
- https://playit.gg/
- https://theboroer.github.io/localtunnel-www/



## serving it locally to public
```
lt --port 8000

npm install -g localtunnel
```
for the password
https://loca.lt/mytunnelpassword


## shortcut snippets and api

```
curl http://localhost:11434/api/generate -d '{"model": "gemma2","prompt": "Why is the sky blue?"}'
```

http://localhost:11434/api/generate
http://localhost:11434/api/chat
```
{
	"model": "qwen2",
	"prompt": "what did you previously say? please explain.",
	"stream": false,
	"format": "json"
}

```


# Claude vs Codex

## useful feedbacks

But the way I utilize both to their strengths is I use GPT as my core developer while using Claude to troubleshoot. I never trust Claude's produced code but I will pass GPTs outputs over to it to analyze and validate what GPT produces and oftentimes Claude will find issues that GPT overlooked or provide recommendations that strengthen the code. Once I get the stamp of approval from both AIs, then I deploy. This method has worked pretty well for me so far. But I wouldn't rely on either alone because GPT is like working with a junior dev with ADD while Claude is like working with a senior dev thats a lazy pathological liar. Claude doesn't want to do the work but it has no problem checking out and validating the work GPT does.