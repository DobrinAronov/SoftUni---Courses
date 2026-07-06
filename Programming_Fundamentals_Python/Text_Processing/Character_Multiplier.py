def multiplier_characters(words_list: list) -> int:
    total = 0
    first_word = words_list[0]
    second_word = words_list[1]
    shortest_length = min([len(word) for word in words_list])
    # Finding the longer word
    the_longer_word = ''
    for word in words_list:
        if len(word) > shortest_length:
            the_longer_word = word
            break
    # Multiplication of ASCII codes representing characters with equal indices
    for idx in range(shortest_length):
        multiple = ord(first_word[idx]) * ord(second_word[idx])
        total += multiple
    # Adding of ASCCI codes of the remaining symbols
    for symbol in the_longer_word[shortest_length:]:
        total += ord(symbol)

    return total


input_list = input().split()

total_sum = multiplier_characters(input_list)
print(total_sum)
