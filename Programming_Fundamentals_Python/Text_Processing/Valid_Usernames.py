def check_length(some_word: str) -> bool:
    if 3 <= len(some_word) <= 16:
        return True
    return False


def check_characters(some_word: str) -> bool:
    for symbol in some_word:
        if not (symbol.isalpha() or symbol.isdigit() or symbol == '-' or symbol == '_'):
            return False
    return True


input_list = input().split(', ')

for word in input_list:
    if check_length(word) and check_characters(word):
        print(word)
