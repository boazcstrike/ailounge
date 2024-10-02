import requests
from langchain_ollama.llms import OllamaLLM
from bs4 import BeautifulSoup
from langchain.agents import Tool
from langchain.prompts import (
  PromptTemplate,
  ChatPromptTemplate,
  SystemMessagePromptTemplate, HumanMessagePromptTemplate,
)
from langchain_community.utilities import SearxSearchWrapper
from langchain.schema import HumanMessage, SystemMessage


class Searcher():
    """A class for performing web searches and analyzing results using a language model."""

    def __init__(self, model):
        self.model = model
        self.summarizer_prompt = PromptTemplate(
            input_variables=["content"],
            template="Summarize the following content in 2-3 sentences with concise and short words including important details:\n\n{content}"
        )
        self.summarizer_chain = self.model | self.summarizer_prompt

        self.query_generator_prompt = PromptTemplate(
            input_variables=["content"],
            template="Generate a 10 word maximum search query based on this content:\n\n{content}\n\nSearch query:"
        )
        self.query_generator_chain = self.model | self.query_generator_prompt

        self.result_parser_prompt = PromptTemplate(
            input_variables=["content"],
            template="Summarize the following web page content in 2-3 sentences:\n\n{content}"
        )
        self.result_parser_chain = self.model | self.result_parser_prompt

    def summarize_content(self, content):
        result = self.summarizer_chain.invoke(content)
        print("\n\n summarize_content result", result)
        return result

    def generate_search_query(self, content):
        result = self.query_generator_chain.invoke(content)
        print("\n\n generate_search_query result", result)
        return result.strip() if isinstance(result, str) else result['text'].strip()

    def search_searxng(self, query):
        response = requests.get(f"http://localhost:8080/search", params={"q": query, "format": "json"})
        print("\n\nresponse", response)
        return response.json()

    def parse_and_summarize_result(self, html_content):
        print("\n\nparse_and_summarize_result html_content", html_content)
        soup = BeautifulSoup(html_content, 'html.parser')
        text_content = soup.get_text()
        print("\n\nparse_and_summarize_result text_content", text_content)
        return self.result_parser_chain.invoke(text_content)

    def process(self, content):
        print(f"\n\nContent: {content}")
        summary = self.summarize_content(content)
        print(f"\n\nContent summary: {summary}")

        search_query = self.generate_search_query(summary)
        print(f"\n\nGenerated search query: {search_query}")

        search_results = self.search_searxng(search_query)
        if search_results['results']:
            first_result = search_results['results'][0]
            html_content = requests.get(first_result['url']).text
            result_summary = self.parse_and_summarize_result(html_content)
            print(f"\n\nSearch result summary: {result_summary}")
        else:
            print("No search results found.")

def main():
    searcher = Searcher(model=OllamaLLM(
        model="bo-instruct",
        temperature=1,
        repeat_last_n=120,
        top_k=75,
    ))
    content = """
    I'm drawn to your challenge of stepping back from a "one-size-fits-all" approach. It's an intriguing idea that speaks directly to the need we're highlighting about making changes within healthcare today. How do you see this line of thinking extending beyond hospitals and into other areas where society often fails? What examples come to mind, what implications would it have?
    """
    searcher.process(content)

if __name__ == "__main__":
    main()
