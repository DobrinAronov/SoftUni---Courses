text = input()
[print(f"{char}: {text.count(char)} time/s") for char in sorted({letter for letter in text})]