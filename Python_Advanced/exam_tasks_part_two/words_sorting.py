def words_sorting(*words: str) -> str:
    words_dict = {}
    for word in words:
        if word not in words_dict:
            value = sum(ord(sym) for sym in word)
            words_dict[word] = value

    output = []
    total_sum = sum(value for value in words_dict.values())
    if total_sum % 2 != 0:
        for key, value in sorted(words_dict.items(), key=lambda x: -x[1]):
            output.append(f"{key} - {value}")
    else:
        for key, value in sorted(words_dict.items()):
            output.append(f"{key} - {value}")

    return '\n'.join(output)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
