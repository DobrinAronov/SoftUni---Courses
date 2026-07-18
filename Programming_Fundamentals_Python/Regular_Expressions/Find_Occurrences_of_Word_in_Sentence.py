import re

def find_count_repeat(some_string: str, searched_word: str):
    pattern = fr"\b{searched_word}\b"
    return re.findall(pattern, some_string, re.I)


input_string = input().lower()
search_word = input().lower()

matches = find_count_repeat(input_string, search_word)
print(len(matches))