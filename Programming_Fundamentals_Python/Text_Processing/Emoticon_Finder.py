def find_emoticons(text: str) -> list:
    emoticons = []

    for idx in range(len(text)):
        if text[idx] == ':':
            emoticon = text[idx] + text[idx + 1]
            emoticons.append(emoticon)
    return emoticons


input_text = input()

found_emoticons = find_emoticons(input_text)

for emoji in found_emoticons:
    print(emoji)
