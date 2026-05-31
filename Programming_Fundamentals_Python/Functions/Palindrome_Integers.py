def palindrome(num: int) -> bool:
    num_to_str = str(num)
    if num_to_str == num_to_str[:: -1]:
        return True
    return False


input_list = [int(element) for element in input().split(', ')]

for number in input_list:
    print(palindrome(number))