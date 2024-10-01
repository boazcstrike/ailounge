import re


def read_file(file_path):
    with open(f"dump/{file_path}", "r") as file:
        content = file.read()
    return content


def parse_contents(contents):
    cleaned_response = re.sub(r"<\|.*?\|>", "", contents)
    cleaned_response = re.sub(r"\[chat#\d+\]\[.*?\]:", "", cleaned_response)
    cleaned_response = re.sub(r"\[.*?\]", "", cleaned_response)
    cleaned_response = re.sub(r"<.*?>", "", cleaned_response)
    cleaned_response = re.sub(r"</.*?>", "", cleaned_response)
    cleaned_response = re.sub(r"<\/.*?>", "", cleaned_response)
    cleaned_response.strip("_")
    return cleaned_response.strip("<|\|>")
