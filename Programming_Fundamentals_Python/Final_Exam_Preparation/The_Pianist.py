def add(pieces: dict, part_to_split: str) -> tuple[dict, str]:
    piece_name, composer_name, key_name = part_to_split.split('|')
    if piece_name not in pieces.keys():
        pieces[piece_name] = {'composer': composer_name, 'key': key_name}
        return pieces, f"{piece_name} by {composer_name} in {key_name} added to the collection!"
    return pieces, f"{piece_name} is already in the collection!"


def remove(pieces: dict, part_to_split: str) -> tuple[dict, str]:
    piece_name = part_to_split
    if piece_name in pieces.keys():
        del pieces[piece_name]
        return pieces, f"Successfully removed {piece_name}!"
    return pieces, f"Invalid operation! {piece_name} does not exist in the collection."


def change_key(pieces: dict, part_to_split: str) -> tuple[dict, str]:
    piece_name, new_key = part_to_split.split('|')
    if piece_name in pieces.keys():
        pieces[piece_name]['key'] = new_key
        return pieces, f"Changed the key of {piece_name} to {new_key}!"
    return pieces, f"Invalid operation! {piece_name} does not exist in the collection."


piano_pieces = {}

number_of_pieces = int(input())
for num in range(number_of_pieces):
    piece, composer, key = input().split('|')
    if piece not in piano_pieces.keys():
        piano_pieces[piece] = {'composer': composer, 'key': key}

while (current_command := input()) != "Stop":
    command, arguments = current_command.split('|', 1)
    message = ''
    if command == "Add":
        piano_pieces, message = add(piano_pieces, arguments)
    elif command == "Remove":
        piano_pieces, message = remove(piano_pieces, arguments)
    elif command == "ChangeKey":
        piano_pieces, message = change_key(piano_pieces, arguments)
    print(message)

for piece, piece_data in piano_pieces.items():
    print(f"{piece} -> Composer: {piece_data['composer']}, Key: {piece_data['key']}")
