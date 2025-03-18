import os
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
from textwrap import dedent
from typing import List

from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.file import FileTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.tools.newspaper import NewspaperTools

from pydantic import BaseModel

from agentsreader import clean_md_to_script
from utils.narrator import Narrator, read_w_edge_tts
from utils.main import read_file


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class Article(BaseModel):
    title: str
    summary: str
    reference_links: List[str]


prefix_file_name = datetime.now().strftime("%m%d%Y%H%M%S")
urls_file = Path(__file__).parent.joinpath("tmp", f"{prefix_file_name}__urls.md")
urls_file.parent.mkdir(parents=True, exist_ok=True)
# model = Ollama(id="llama3.1:8b-instruct-q8_0")
# model = Ollama(id="llama3.1-instruct-steroids")
# model = Ollama(id="llama3.1-instruct-weakened")
# model = Ollama(id="QW-6X1.5B-DeepSeek-Qwen-LAM-e32-Q4_K_S") # does not support tools
model = OpenAIChat(id="gpt-4o-mini", api_key=OPENAI_API_KEY)
# model = OpenAIChat(
#     id="grok-2-latest",
#     api_key=OPENAI_API_KEY,
#     base_url="https://api.x.ai/v1",
# )


def askainews() -> None:
    journalist = Agent(
        name="Journalist",
        model=model,
        role="Searches the top URLs for a topic",
        instructions=[
            "Given a topic, first generate a list of 3 search terms related to that topic.",
            "For each search term, search the web and analyze the results. Return the 5 most relevant URLs to the topic.",
            "You are writing for the New York Times, so the quality of the sources is important.",
        ],
        tools=[DuckDuckGoTools()],
        save_response_to_file=str(urls_file),
        add_datetime_to_instructions=True,
        markdown=True,  # unsure as this was removed
    )
    researches_url_file = Path(__file__).parent.joinpath("tmp", f"{prefix_file_name}__researches.md")
    researcher = Agent(
        name="Researcher",
        model=model,
        tools=[
            NewspaperTools(),
        ],
        role="Researches and validates the authenticity of the given urls.",
        description="You are a distinguished research scholar with expertise in multiple disciplines.",
        instructions=dedent(
            f"""\
                - Conduct a research on all of the given urls in {urls_file.name}
                - Synthesize findings across sources
                - You are checking and writing for the New York Times, so the quality of the sources is important.
            """
        ),
        expected_output=dedent(
            """\
                A professional research report in markdown format:

                # {Compelling Title That Captures the Topic's Essence}

                ## Introduction
                {Context and importance of the topic}

                ## Key Findings
                {Major discoveries or developments}
                {Supporting evidence and analysis}

                ## Key Takeaways
                - {Bullet point 1}
                - {Bullet point 2}
                - {Bullet point 3}
                - ...

                ## Sources
                - [Source 1](link) - Key finding/quote
                - [Source 2](link) - Key finding/quote
                - [Source 3](link) - Key finding/quote
                - ...

                ---
                Date: {current_date}\
            """
        ),
        add_datetime_to_instructions=True,
        show_tool_calls=True,
        markdown=True,
        save_response_to_file=str(researches_url_file),
    )
    writer = Agent(
        name="Writer",
        model=model,
        role="Writes a high-quality article",
        description=(
            "You are a senior writer for the New York Times. Given a topic and a list of URLs, "
            "your goal is to write a high-quality NYT-worthy article on the topic."
        ),
        instructions=[
            f"First read all urls in {urls_file.name} using `get_article_text`."
            "Then write a high-quality NYT-worthy article on the topic."
            "The article should be well-structured, informative, engaging, and catchy.",
            f"Ensure you provide a nuanced and balanced opinion, quoting facts where possible referencing -- {researches_url_file.name}",
            "Ensure the length is at least as long as a NYT cover story -- at a minimum, 10 paragraphs.",
            "Focus on clarity, coherence, and overall quality.",
            "Never make up facts or plagiarize. Always provide proper attribution.",
            "Remember: you are writing for the New York Times, so the quality of the article is important.",
        ],
        tools=[Newspaper4kTools(), FileTools(base_dir=urls_file.parent)],
        add_datetime_to_instructions=True,
        markdown=True,  # unsure as this was removed
    )

    reporter = Agent(
        name="Reporter",
        model=model,
        team=[journalist, researcher, writer],
        description="You are a senior editor with PhD in Computer Engineering, Computer Science. Given a topic, your goal is to report a world-class worthy article.",
        instructions=[
            "First ask the search journalist to search for the most relevant URLs for that topic.",
            "Then ask the writer to get an engaging draft of the article.",
            "Ensure the researcher cross-verifies all claims and data with reliable, fact-based sources.",
            "Edit, proofread, and refine the article into a script to ensure it meets the high world class standards",
            "The script should be extremely articulate and well written.",
            "Do not hesitate to use technical terminology.",
            "Next, eliminate any unnecessary syntax, emoticons and enumerations to craft the best reporting script.",
            "Focus on clarity, coherence, and overall quality.",
            "Remember: you are the final gatekeeper before the script is published, so make sure the script is perfect.",
        ],
        add_datetime_to_instructions=True,
        markdown=True,
        # debug_mode=True,
        save_response_to_file=str(
            Path(__file__).parent.joinpath("tmp", f"{prefix_file_name}_results.md")
        ),
    )

    input_prompt = input("Topic to start with?\n💬: ")
    reporter.print_response(input_prompt, stream=True)

    content = read_file(f"{prefix_file_name}__results.md")
    content = clean_md_to_script(content)
    read_w_edge_tts(content)


if __name__ == "__main__":
    askainews()


def threat_agents_sample():
    from agno.agent import Agent
    from agno.models.google import Gemini
    from agno.tools.exa import ExaTools
    from agno.storage.agent.postgres import PostgresAgentStorage
    import os
    import getpass

    # Database setup with system user
    DB_USER = getpass.getuser()  # Gets current system username
    DB_PASS = ""
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "agno"


    # Define RSS feeds
    FEEDS = {
        "nvd": "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss.xml",
        "us_cert": "https://www.cisa.gov/uscert/ncas/alerts.xml",
    }
    # Database setup for session persistence
    storage = PostgresAgentStorage(
        table_name="threat_intel_sessions",
        db_url=f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
        # db_url="postgresql+psycopg://agno:@localhost:5432/ai"
    )

    # Agent 1: Web Search Agent
    web_agent = Agent(
        name="WebSearchAgent",
        model=Gemini(id="gemini-2.0-flash"),
        tools=[ExaTools()],
        instructions=[
            "Search the web for cybersecurity threat reports from the last 7 days.",
            "Include a variety of threats (e.g., ransomware, phishing, vulnerabilities), not just one group.",
            "Return findings in concise markdown format with URLs.",
        ],
        show_tool_calls=False,  # Hide tool execution details in output
        markdown=True,
    )

    # Agent 2: X Analysis Agent
    x_agent = Agent(
        name="XAnalysisAgent",
        model=Gemini(id="gemini-2.0-flash"),
        instructions=[
            "Analyze recent X posts for mentions of cybersecurity threats.",
            "Cover a range of threats, not limited to a single group.",
            "Return findings in concise markdown format with timestamps and usernames.",
        ],
        show_tool_calls=False,
        markdown=True,
    )
    # Agent 3: Feed Reader Agent
    feed_agent = Agent(
        name="FeedReaderAgent",
        model=Gemini(id="gemini-2.0-flash"),
        tools=[ExaTools()],
        instructions=[
            "Search for recent cybersecurity updates from NVD (nvd.nist.gov) and US-CERT (cisa.gov).",
            f"Alternatively, if you can fetch directly, retrieve content from: {', '.join(FEEDS.values())}.",
            "Summarize key vulnerabilities or alerts in concise markdown format.",
            "Include source (NVD or US-CERT) and titles of updates.",
        ],
        show_tool_calls=False,
        markdown=True,
    )


    # Agent 4: Summary Agent (Team Leader)
    summary_agent = Agent(
        name="SummaryAgent",
        model=Gemini(id="gemini-2.0-flash"),
        team=[web_agent, x_agent, feed_agent],  # Added FeedReaderAgent to the team
        storage=storage,
        instructions=[
            "Combine findings from WebSearchAgent, XAnalysisAgent, and FeedReaderAgent into a single report.",
            "Format the report in markdown with the following structure:",
            "- Header: 'Threat Intelligence Report'",
            "- Timestamp: Current date and time",
            "- Sections: 'Summary', 'Threat Actors', 'Targeted Industries', 'Attack Vectors', 'TTPs', 'Feed Updates'",
            "Include a variety of recent cybersecurity threats in all sections.",
            "Ensure the output is clean and readable.",
        ],
        show_tool_calls=False,
        markdown=True,
        add_history_to_messages=True,
    )


    # Execute and print the response cleanly
    response = summary_agent.print_response(
        "Provide a threat intelligence report on recent cybersecurity threats",
        # "Provide a threat intelligence report on recent cybersecurity threats, focusing on the Clop ransomware group.",
        stream=False,  # Non-streaming for a complete, polished output
    )
