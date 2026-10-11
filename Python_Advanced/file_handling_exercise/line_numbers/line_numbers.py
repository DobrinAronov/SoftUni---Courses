from string import punctuation

output_list = []

with open("text.txt", "r") as text:
    for idx, sentence in enumerate(text, start=1):
        letters = len([symbol for symbol in sentence if symbol.isalpha()])
        punc = len([symbol for symbol in sentence if symbol in punctuation])

        output_list.append(f"Line {idx}: {sentence.strip()} ({letters})({punc})\n")

with open("output.txt", "w") as output:
    for sentence in output_list:
        output.write(sentence)