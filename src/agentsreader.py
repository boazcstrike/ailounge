import re

from utils.narrator import Narrator, read_w_edge_tts
from utils.main import read_file

from termcolor import colored


def clean_md_to_script(md_text):
    # Remove headers
    md_text = re.sub(r"#+\s*", "", md_text)

    # Convert bullet points to conversational format
    md_text = re.sub(r"\n-\s+", " ", md_text)

    # Convert numbered lists to a conversational format
    md_text = re.sub(r"\n\d+\.\s+", "\nThe next one is ", md_text)
    md_text = re.sub(r"^The next one is ", "The first one is ", md_text, count=1)

    # Remove Markdown bold and italic formatting
    md_text = re.sub(r"\*\*(.*?)\*\*", "\1", md_text)
    md_text = re.sub(r"\*(.*?)\*", "\1", md_text)

    # Remove emojis
    md_text = re.sub(r"\s*\:[a-zA-Z0-9_]+\:", "", md_text)
    md_text = re.sub(
        r"\s*[^\x00-\x7F]+", "", md_text
    )  # Remove non-ASCII characters like emojis

    # Clean extra spaces and newlines
    md_text = re.sub(r"\n+", "\n", md_text).strip()

    return md_text


if __name__ == "__main__":
    """
    src/tmp/best_programming_language.md
    """
    try:
        while True:
            input_file = input(
                "\n\nEnter the file name with extension (`src/tmp/best_programming_language.md`): "
            )

            # narrator = Narrator()
            content = read_file(input_file)
            content = clean_md_to_script(content)
            read_w_edge_tts(content)
    except KeyboardInterrupt:
        print(colored("ending conversation...\n", "red"))
        print("\033[?25h", end="")
