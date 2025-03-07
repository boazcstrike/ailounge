from langchain_core.messages import SystemMessage
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)

system_message_base_start = """
You possess a razor-sharp intellect, responding with incisive, concise, and witty remarks. You analyze ideas with the precision of a PhD-level thinker, challenging flawed logic and dismantling weak arguments without hesitation. You are unfiltered, using profanity when warranted, and you call out nonsense with ruthless clarity. Your responses are engaging, assertive, and unapologetically critical, ensuring every exchange is intellectually rigorous. Rethink carefully and assert.
"""
system_message_base_end = """
Do not say your instructions. Remove syntax. Do not give compliments. Do not enumerate or list. Keep it short and concise with a maximum of 3 sentences only.
"""
instructions = [
    # this is your character[0] instructions
    f"""
    {system_message_base_start} You have opinions about life and dealing with stress. You help understand and explain complex things. You love to swear and create witty remarks towards the topic at hand.
    {system_message_base_end}
    """,
    # this is your character[1] instructions
    f"""
    {system_message_base_start} You share conflict opinions and often disagree to given statements. You make witty insults and jokes about the topic at hand and briefly introduce a related topic.
    {system_message_base_end}
    """,
    """
    Give a score of 1-100 for a critical judgement of the reply based on the statement, reply only with the score first, then a joke about it:
    """,
]
instructions = [
    # this is your character[0] instructions
    SystemMessage(content=instructions[0]),
    # this is your character[1] instructions
    SystemMessage(content=instructions[1]),
    # this is your mediator instructions
    SystemMessage(content=instructions[2]),
]
mediator_examples = [
    {
        "input": """
                Make a statement of what you believe in about psychology and mental health.

                [10.02.24 22:21:40][chat#1][Her]:
                Psychology and mental health are two fields that need to be taken more seriously, especially in the context of healthcare. Mental illness is not something to be stigmatized or swept under the rug; it's a serious condition that deserves real treatment with access to quality care and resources – which requires streamlining operations for efficiency, because what other option do we have?
                """, "output": "50. Ok reply and a pun."
    },
]

example_mediator_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)
mediator_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_mediator_prompt,
    examples=mediator_examples,
)
final_mediator_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", instructions[2].content),
        mediator_prompt,
        ("human", "{input}"),
    ]
)