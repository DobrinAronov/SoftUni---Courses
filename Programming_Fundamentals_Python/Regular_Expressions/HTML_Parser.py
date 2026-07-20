import re


def find_title(some_string: str) -> str:
    pattern = r"(?<=<title>)(?P<title>\w+(?:\s\w+)*)(?=</title>)"
    matches = re.findall(pattern, some_string)
    return ''.join(matches)


def find_content(some_string: str) -> str:
    pattern = r"(?<=<body>)(?P<content>[\s\S]+)(?=</body>)"
    selected_text = ''.join(re.findall(pattern, some_string))
    clean_text = r"<[^>]*>|\n|\\n"
    output_text = re.sub(clean_text, '', selected_text)
    return output_text


input_string = input()

extracted_title = find_title(input_string)
extracted_content = find_content(input_string)

print(f"Title: {extracted_title}")
print(f"Content: {extracted_content}")
