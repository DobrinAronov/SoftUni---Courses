def move(some_string: str, num: int) -> str:
    output_string = some_string[num:] + some_string[:num]
    return output_string


def insert(some_string: str, idx: int, insert_str: str) -> str:
    output_string = some_string[:idx] + insert_str + some_string[idx:]
    return output_string


def change_all(some_string: str, sub_str: str, replace: str) -> str:
    output_string = some_string.replace(sub_str, replace)
    return output_string


encrypted_message = input()

while (current_command := input()) != "Decode":
    current_instruction = current_command.split('|')
    action = current_instruction[0]

    if action == 'Move':
        number_of_letters = int(current_instruction[1])
        encrypted_message = move(encrypted_message, number_of_letters)

    elif action == 'Insert':
        index, value = int(current_instruction[1]), current_instruction[2]
        encrypted_message = insert(encrypted_message, index, value)

    elif action == 'ChangeAll':
        substring, replacement = current_instruction[1], current_instruction[2]
        encrypted_message = change_all(encrypted_message, substring, replacement)

print(f"The decrypted message is: {encrypted_message}")