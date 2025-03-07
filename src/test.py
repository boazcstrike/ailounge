from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import requests
from bs4 import BeautifulSoup

class Searcher:
    def __init__(self, model="llama2", searxng_url="https://searx.be"):
        self.model = Ollama(model=model)
        self.searxng_url = searxng_url

        self.summarizer_prompt = PromptTemplate(
            input_variables=["content"],
            template="Summarize the following content in 2-3 sentences:\n\n{content}"
        )
        self.summarizer_chain = LLMChain(llm=self.model, prompt=self.summarizer_prompt)

        self.query_generator_prompt = PromptTemplate(
            input_variables=["content"],
            template="Generate a search query based on this content:\n\n{content}\n\nSearch query:"
        )
        self.query_generator_chain = LLMChain(llm=self.model, prompt=self.query_generator_prompt)

        self.result_parser_prompt = PromptTemplate(
            input_variables=["content"],
            template="Summarize the following web page content in 2-3 sentences:\n\n{content}"
        )
        self.result_parser_chain = LLMChain(llm=self.model, prompt=self.result_parser_chain)

    def summarize_content(self, content):
        return self.summarizer_chain.run(content)

    def generate_search_query(self, content):
        return self.query_generator_chain.run(content)

    def search_searxng(self, query):
        response = requests.get(f"{self.searxng_url}/search", params={"q": query, "format": "json"})
        return response.json()

    def parse_and_summarize_result(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        text_content = soup.get_text()
        return self.result_parser_chain.run(text_content)

    def process(self, content):
        summary = self.summarize_content(content)
        print(f"Content summary: {summary}")

        search_query = self.generate_search_query(content)
        print(f"Generated search query: {search_query}")

        search_results = self.search_searxng(search_query)
        if search_results['results']:
            first_result = search_results['results'][0]
            html_content = requests.get(first_result['url']).text
            result_summary = self.parse_and_summarize_result(html_content)
            print(f"Search result summary: {result_summary}")
        else:
            print("No search results found.")

def main():
    searcher = Searcher()
    content = "Your input content here"
    searcher.process(content)

if __name__ == "__main__":
    main()