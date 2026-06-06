def find_substrings(frs_list: list[str], sec_list: list[str]) -> list[str]:
    output_list = []
    for frs_word in frs_list:
        for sec_word in sec_list:
            if frs_word in sec_word:
                output_list.append(frs_word)
                break
    return output_list


first_string = input().split(", ")
second_string = input().split(", ")

print(find_substrings(first_string, second_string))
