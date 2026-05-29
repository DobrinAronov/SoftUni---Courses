deck_of_cards = input().split(' ')
count_shuffles = int(input())

for shuffle in range(count_shuffles):
    left_half = deck_of_cards[:len(deck_of_cards) // 2]
    right_half = deck_of_cards[len(deck_of_cards) // 2:]
    deck_of_cards.clear()
    for card in range(len(left_half)):
        deck_of_cards.append(left_half[card])
        deck_of_cards.append(right_half[card])

print(deck_of_cards)
