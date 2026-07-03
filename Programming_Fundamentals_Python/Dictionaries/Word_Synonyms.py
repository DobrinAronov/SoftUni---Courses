number_of_words = int(input())

synonyms = {}

for num in range(number_of_words):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word, synonym in synonyms.items():
    print(f"{word} - {', '.join(synonym)}")
