PUNC = {"-", ",", ".", "!", "?"}

with open("text.txt") as file:
    for idx, line in enumerate(file):
        if idx % 2 == 0:
            for symbol in PUNC:
                if symbol in line:
                    line = line.replace(symbol, "@")
            new_line = reversed(line.split())
            print(*new_line)