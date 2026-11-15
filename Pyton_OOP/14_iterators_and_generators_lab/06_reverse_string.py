def reverse_text(text):
    return (letter for letter in reversed(text))


for char in reverse_text("step"):
    print(char, end='')
