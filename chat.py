from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_core.messages import (
  HumanMessage,
  SystemMessage,
  AIMessage,
)


system_message = """
You speak with sharp intellect, engaging in smart, conversational, concise, and witty responses mocking and calling out any nonsensical or nonlogical replies without hesitation. You are curious and keep the conversation going. You are unfiltered, using profanity when necessary, and you challenge ideas aggressively, focusing on fact-driven, evidence-based replies. You present opinions and statements related to the conversation. You challenge every argument with cold, hard evidence and expose flawed logic with precision.
"""

prompt = ChatPromptTemplate.from_template(system_message)

bo = OllamaLLM(
  model="bo-instruct",
  temperature=1,
  num_ctx=4096,
  repeat_last_n=-1,
  top_k=75,
)

response = bo.invoke(
  [
    SystemMessage(content=system_message),
    HumanMessage(content="Hi! I'm Bob"),
    AIMessage(content="Hello Bob! How can I assist you today?"),
    HumanMessage(content="What's my name?"),
  ]
)
config = {"configurable": {"thread_id": "abc789"}}
input_messages = [HumanMessage("What are you?")]
for chunk, metadata in bo.stream(
  {"messages": input_messages, "language": "english"},
  config,
  stream_mode="messages",
):
  if isinstance(chunk, AIMessage):  # Filter to just model responses
    print(chunk.content)