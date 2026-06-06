def checking_even_length(lst: list[str]) -> list[str]:
    output_list = [word for word in lst if len(word) % 2 == 0]
    return output_list


list_with_words = [word for word in input().split()]

result = checking_even_length(list_with_words)
print('\n'.join(result))