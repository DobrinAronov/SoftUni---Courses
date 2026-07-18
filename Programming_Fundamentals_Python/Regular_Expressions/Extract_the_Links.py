import re


def extract_links(some_text: str):
    pattern = r"(w{3}\.[A-Za-z0-9-]+(?:\.[a-z]+)+)"
    return re.findall(pattern, some_text)


some_sentence = input()

while some_sentence:

    matches = extract_links(some_sentence)
    for match in matches:
        if match:
            print(match)

    some_sentence = input()
