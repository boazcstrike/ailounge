import re
from datetime import datetime


def read_file(file_path):
    """
    Read the contents of a file from the 'dump' directory.

    Args:
        file_path (str): The name of the file to read.

    Returns:
        str: The contents of the file.
    """
    with open(f"dump/{file_path}", "r") as file:
        content = file.read()
    return content


def save_file(responses, timestamp):
    """
    Save the responses to a file with a timestamp.

    Args:
        responses (list): A list of response strings to be saved.

    Returns:
        None

    This function creates a new file in the 'dump' directory with a timestamp
    in the filename. It writes each response from the input list to the file,
    and prints a confirmation message with the file path.
    """
    file_path = f"dump/response_{timestamp}.txt"
    # print("responses: ", responses[:50], "...", responses[-50:])
    with open(file_path, "w") as file:
        responses = "\n".join(responses)
        file.write(f"{responses}\n")
        print(f"\n[{datetime.now().strftime('%m/%d/%y %H:%M:%S')}] saved to {file_path}\n")


def parse_contents(contents):
    """
    Parse and clean the contents of a file.

    Args:
        contents (str): The raw contents of the file to be parsed.

    Returns:
        str: The cleaned and parsed contents.

    This function removes various tags, markers, and special characters from the input text,
    including chat markers, HTML-like tags, and other formatting elements.
    """
    cleaned_response = re.sub(r"<\|.*?\|>", "", contents)
    cleaned_response = re.sub(r"\[chat#\d+\]\[.*?\]:", "", cleaned_response)
    cleaned_response = re.sub(r"\[.*?\]", "", cleaned_response)
    cleaned_response = re.sub(r"<.*?>", "", cleaned_response)
    cleaned_response = re.sub(r"</.*?>", "", cleaned_response)
    cleaned_response = re.sub(r"<\/.*?>", "", cleaned_response)
    cleaned_response.strip("_")
    return cleaned_response.strip("<|\|>")
