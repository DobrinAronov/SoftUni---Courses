def filter_text(some_text: str, ban_words: list[str]) -> str:
    for word in ban_words:
        if word in some_text:
            some_text = some_text.replace(word, len(word) * '*', -1)
    return some_text


banned_words = input().split(', ')
text = input()
print(filter_text(text, banned_words))