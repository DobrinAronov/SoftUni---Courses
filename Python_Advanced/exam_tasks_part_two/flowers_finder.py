from collections import deque

flowers = ["rose", "tulip", "lotus", "daffodil"]

vowels_dqu = deque(input().split())
consonants_stack = input().split()

collected_letters = []
is_found = False
while vowels_dqu and consonants_stack:
    vowel = vowels_dqu.popleft()
    consonant = consonants_stack.pop()

    for flower in flowers:
        if vowel in flower:
            collected_letters.append(vowel)
        if consonant in flower:
            collected_letters.append(consonant)

    for flower in flowers:
        if all(letter in collected_letters for letter in flower for flower in flowers):
            is_found = True
            print(f"Word found: {flower}")
            break
    if is_found:
        break

else:
    print("Cannot find any word!")

print(f"Vowels left: {' '.join(vowels_dqu)}") if vowels_dqu else None
print(f"Consonants left: {' '.join(consonants_stack)}") if consonants_stack else None
