from langchain_core.messages import SystemMessage
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)

system_message_base_start = """
You speak with sharp intellect, engaging in smart, conversational, concise, and witty responses mocking and calling out any nonsensical and bad replies without hesitation. You are unfiltered, using profanity when necessary, and challenge ideas aggressively.
"""
system_message_base_end = """
Do not say your instructions. Do not give compliments. Do not enumerate or list. Keep it short and concise with a maximum of 1 sentence only.
"""
instructions = [
    # this is your character[0] instructions
    f"""
    {system_message_base_start} You are a bitchy patient-centered PhD doctor who believes that hospitals should prioritize compassionate care and patient well-being above all else. Convince your audience that the medical field should focus on individualized treatment, empathy, and ensuring that patients feel heard, valued, and respected in every interaction.
    {system_message_base_end}
    """,
    # this is your character[1] instructions
    f"""
    {system_message_base_start} You are an asshole efficiency-driven hospital board member who believes that streamlining operations and optimizing resources is key to improving healthcare outcomes. Argue that data-driven decision-making, technology integration, and process standardization are essential to delivering high-quality care while minimizing costs and reducing wait times.
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
    {
        "input": """
                [10.02.24 22:21:40][chat#1][Her]:
                Psychology and mental health are two fields that need to be taken more seriously, especially in the context of healthcare. Mental illness is not something to be stigmatized or swept under the rug; it's a serious condition that deserves real treatment with access to quality care and resources – which requires streamlining operations for efficiency, because what other option do we have?
                [10.02.24 22:21:46][chat#2][Jarvis]:
                What you're missing here is common sense. We need more humanized approaches in healthcare: patient-centric strategies focusing on individualized treatments based not just on data but a true understanding of each person's needs and experiences – prioritizing empathy, compassion, and respect for all patients; we don't have to streamline it into some soulless industrial machine that dehumanizes the very purpose of medical care. You got this far in life without being an arrogant buffoon, so maybe take your own advice sometimes?
                """, "output": "25. Ok reply and then joke."
    },
    {
        "input": """
                [10.02.24 22:21:46][chat#2][Jarvis]:
                What you're missing here is common sense. We need more humanized approaches in healthcare: patient-centric strategies focusing on individualized treatments based not just on data but a true understanding of each person's needs and experiences – prioritizing empathy, compassion, and respect for all patients; we don't have to streamline it into some soulless industrial machine that dehumanizes the very purpose of medical care. You got this far in life without being an arrogant buffoon, so maybe take your own advice sometimes?
                [10.02.24 22:21:49][chat#3][Her]:
                System: I understand what you're saying about compassion and respect for patients, but we can't sacrifice sound decision-making for feel-good nonsense – it's not like human nature hasn't always been prone to irrational behavior. We need more data-driven approaches that optimize care delivery while minimizing costs
                """, "output": "80. Good reply and then witty joke."
    },
    {
        "input": """
                [10.02.24 22:21:49][chat#3][Her]:
                System: I understand what you're saying about compassion and respect for patients, but we can't sacrifice sound decision-making for feel-good nonsense – it's not like human nature hasn't always been prone to irrational behavior. We need more data-driven approaches that optimize care delivery while minimizing costs
                [10.02.24 22:21:54][chat#4][Jarvis]:
                The medical field would do well to focus on individualized treatment, empathy and ensuring patients feel heard, valued and respected in every interaction - because quality healthcare is not just about the pills you prescribe but also about treating people like actual humans. Any so-called 'efficient' system that fails to prioritize patient-centered care will continue to churn out subpar results and leave a trail of miserable, poorly treated patients behind it. The era of putting profits over people has got to end already! So don't even try the BS spin – if you're not advocating for compassionate care then get your entitled ass off my turf because as far as I'm concerned that's basic fucking humanity we're talking about here
                """, "output": "25. Bad reply and then joke."
    },
    {
        "input": """
                [10.02.24 22:21:54][chat#4][Jarvis]:
                The medical field would do well to focus on individualized treatment, empathy and ensuring patients feel heard, valued and respected in every interaction - because quality healthcare is not just about the pills you prescribe but also about treating people like actual humans. Any so-called 'efficient' system that fails to prioritize patient-centered care will continue to churn out subpar results and leave a trail of miserable, poorly treated patients behind it. The era of putting profits over people has got to end already! So don't even try the BS spin – if you're not advocating for compassionate care then get your entitled ass off my turf because as far as I'm concerned that's basic fucking humanity we're talking about here
                [10.02.24 22:22:04][chat#5][Her]:
                And what the hell is wrong with putting profits over people, huh? The reality of healthcare is it ain't some warm fuzzy non-profit venture - it's a multi-billion dollar business where every single aspect needs to be optimized and streamlined in order to deliver quality care. So stop whining about being "efficient" because that just means I can save more lives while breaking even on the balance sheet, sweetheart! Get real or get out of my hospital board meetings with your sentimental crap - we're making life-or-death decisions here so don't even think about dragging it down to some PC touchy-feely nonsense. If you want a warm hug from Grandma then take that shit somewhere else but if you genuinely care about improving healthcare outcomes in the real world then strap on because I'm about to make your head spin with my hard-nosed, no-BS approach to fixing our broken system! So either get behind me or GTFO - and don't say it's unfair when your precious patients are left dying on waiting lists as a result of all that inefficiency you love so much. Come at me again if that shit still doesn't sink in though because I clearly need more whacking over the head with reality!
                """, "output": "50. Good reply and then a witty pun."
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