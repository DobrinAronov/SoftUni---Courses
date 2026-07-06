def extract_file(input_list: list) -> tuple[str, str]:
    name = ''
    extension = ''
    for check_string in input_list:
        if '.' in check_string:
            idx = check_string.index('.')
            name = check_string[:idx]
            extension = check_string[idx + 1:]
    return name, extension


input_path = input().split('\\')

file_name, file_extension = extract_file(input_path)
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")