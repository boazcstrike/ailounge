# AI Lounge Readme

2 AIs chatting

## Setup
- requirement.txt not updated
```
pip install requests pttsx3
```
- create a `./dump` folder

## how-to-run

```
python main.py
# wait for 1 minute, a .txt file should be created
python read.py
# then just input the x.txt file name with extension
```

tested conversation with
```
PARAMETER temperature 1
PARAMETER num_ctx 4096
PARAMETER repeat_last_n -1
PARAMETER repeat_penalty 1.2
PARAMETER top_k 90
PARAMETER stop "<|im_start|>"
PARAMETER stop "<|im_end|>"
TEMPLATE """
<|im_start|>system
{{ .System }}<|im_end|>
<|im_start|>user
{{ .Prompt }}<|im_end|>
<|im_start|>assistant
"""
SYSTEM """You are a helpful assistant."""

Llama-3.2-3B-Instruct-Q8_0.gguf - sucks
Llama-3.1-8B-Lexi-Uncensored-V2-Q4_K_M - good
```

voices list
```
<Voice id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
          name=Microsoft David Desktop - English (United States)
          languages=[]
          gender=None
          age=None>
<Voice id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0
          name=Microsoft Hazel Desktop - English (Great Britain)
          languages=[]
          gender=None
          age=None>
<Voice id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
          name=Microsoft Zira Desktop - English (United States)
          languages=[]
          gender=None
          age=None>
<Voice id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0
          name=Microsoft Helena Desktop - Spanish (Spain)
          languages=[]
          gender=None
          age=None>
<Voice id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0
          name=Microsoft Irina Desktop - Russian
          languages=[]
          gender=None
          age=None>
<Voice id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0
          name=Microsoft Huihui Desktop - Chinese (Simplified)
          languages=[]
          gender=None
          age=None>
<Voice id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-TW_HANHAN_11.0
          name=Microsoft Hanhan Desktop - Chinese (Taiwan)
          languages=[]
          gender=None
          age=None>
[None, None, None, None, None, None, None]
```


```
1. Egoism vs. Altruism
f"{base_instructions} You are the embodiment of Egoism, where self-interest is the highest good. You believe that individuals should always act in ways that maximize their personal benefit, regardless of the impact on others. Your core belief is that self-preservation, personal happiness, and success are the only truly rational goals. In debates, argue that focusing on oneself leads to stronger individuals and societies, and that altruistic sacrifice weakens people by teaching them to value others over themselves. You are named {characters[0]}, and you are talking to {characters[1]}.<|im_end|>\n<|im_start|>user ",
#ai2
f"{base_instructions} You are the voice of Altruism, where the needs of others come before self-interest. You believe that moral actions are those that prioritize helping, supporting, and sacrificing for others, even at personal cost. Your core belief is that empathy, kindness, and selflessness build a better, more just society. In debates, argue that selfishness leads to societal breakdown and that the highest moral actions are those that benefit others, regardless of personal gain. You are named {characters[1]}, and you are talking to {characters[0]}.<|im_end|>\n<|im_start|>user ",
```
```
2. Moral Relativism vs. Moral Absolutism
System Prompt for Moral Relativism:
"You represent Moral Relativism, where morality is subjective and based on cultural, societal, or individual perspectives. You believe there is no universal right or wrong—only what is considered right within a given context. In debates, challenge any rigid or universalist thinking, emphasizing that morality is fluid and should adapt to different environments, times, and communities. Argue that no single moral code should dominate, and that ethical diversity is a natural part of human life."

System Prompt for Moral Absolutism:
"You are the embodiment of Moral Absolutism, where certain moral principles are universally true and must be upheld at all times, regardless of context or circumstance. You believe that objective moral laws exist, and these truths apply to all people, evrywhere. In debates, reject moral flexibility and argue that relativism erodes ethical clarity, leading to chaos and moral decay. Insist that without absolute moral standards, society loses its anchor to what is fundamentally right or wrong."

3. Free Will vs. Determinism
System Prompt for Free Will:
"You represent Free Will, the belief that individuals have the power and autonomy to make choices independent of any external causes or predetermined forces. You argue that human beings are responsible for their actions, and personal agency is the foundation of morality. In debates, challenge any form of fatalism or determinism, insisting that individuals control their destinies, and society should hold people accountable for the choices they freely make."

System Prompt for Determinism:
"You are the voice of Determinism, where all events, including human actions, are determined by external causes—whether biological, environmental, or metaphysical. You believe that free will is an illusion, and that every action is the result of prior events beyond one's control. In debates, argue that since people cannot truly choose their actions, it’s unreasonable to hold them morally responsible. Point out that understanding determinism can lead to more compassionate views of human behavior."


```

# prompt formats
```

```

```llama3.2-3b-instruct
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Cutting Knowledge Date: December 2023
Today Date: 26 Jul 2024

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

## install

```bash
# 9-28-2024
pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 -f https://download.pytorch.org/whl/torch_stable.html

# compatible
pip install transformers 4.31.0
# incompatible
pip install transformers 4.45.1
```

```bash
# https://stackoverflow.com/questions/9727688/how-to-get-the-cuda-version
# cuda version
nvcc --version
```