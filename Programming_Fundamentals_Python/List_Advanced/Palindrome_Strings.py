def find_palindrome(lst: list[str], find_word: str):
    palindrome_lst = []

    for lst_word in lst:
        if lst_word == lst_word[:: -1]:
            palindrome_lst.append(lst_word)

    count_find_word = palindrome_lst.count(find_word)
    return palindrome_lst, f"Found palindrome {count_find_word} times"


input_strings = [word for word in input().split()]
palindrome_word = input()

palindrome_list, message = find_palindrome(input_strings, palindrome_word)
print(f"{palindrome_list}\n{message}")
