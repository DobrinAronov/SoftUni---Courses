import re

def extract_emails(some_text: str):
    pattern = r"(\s([a-z0-9])([\w\.-]+)@([a-z-]+\.)+\b[a-z]+)"
    return re.findall(pattern, some_text)

text = input()
matches = extract_emails(text)

for match in matches:
    print(match[0].strip())