words = input().lower().split()

output_word =[]

for word in words:
    if words.count(word) % 2 != 0:
        if word not in output_word:
            output_word.append(word)

print(' '.join(output_word))