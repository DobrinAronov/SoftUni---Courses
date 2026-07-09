def html(start_separator: str, final_separator: str, some_string: str) -> str:
    return f"{start_separator}\n    {some_string}\n{final_separator}"


title = input()
content = input()

print(html('<h1>', '</h1>', title))
print(html('<article>', '</article>', content))

while (current_string := input()) != 'end of comments':
    print(html('<div>', '</div>', current_string))
