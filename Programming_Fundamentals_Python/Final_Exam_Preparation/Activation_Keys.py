def contains(text: str, part_for_split: str) -> tuple[str, str]:
    substring = part_for_split
    if substring in text:
        return text, f"{text} contains {substring}"
    return text, "Substring not found!"


def flip(text: str, part_for_split: str) -> tuple[str, str]:
    letter_case, start_idx, end_idx = part_for_split.split(">>>")
    start_idx, end_idx = int(start_idx), int(end_idx)

    changing_part = ''
    for letter in text[start_idx:end_idx]:
        if letter_case == 'Upper':
            changing_part += letter.upper()
        elif letter_case == 'Lower':
            changing_part += letter.lower()

    text = text[:start_idx] + changing_part + text[end_idx:]
    return text, ''


def text_slice(text: str, part_for_split: str) -> tuple[str, str]:
    start_idx, end_idx = part_for_split.split(">>>")
    start_idx, end_idx = int(start_idx), int(end_idx)

    text = text[:start_idx] + text[end_idx:]
    return text, ''


all_commands = {
    'Contains': contains,
    'Flip': flip,
    'Slice': text_slice
}

activation_key = input()

while (current_command := input()) != "Generate":
    command, arguments = current_command.split(">>>", 1)
    activation_key, message = all_commands[command](activation_key, arguments)
    if message:
        print(message)
    else:
        print(activation_key)

print(f"Your activation key is: {activation_key}")
