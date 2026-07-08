def check_length(some_ticket: str) -> bool:
    if len(some_ticket) == 20:
        return True
    return False


def check_half_ticket(half_ticket: str) -> tuple[str, int]:
    winning_symbol = ''
    number_of_repeat = 0

    current_win_symbol = ''
    current_win_count = 0

    for idx in range(len(half_ticket)):
        symbol = half_ticket[idx]
        if not current_win_symbol:
            if symbol in ['@', '#', '$', '^']:
                current_win_symbol = symbol
                current_win_count += 1
            else:
                continue
        elif symbol == half_ticket[idx - 1] == current_win_symbol:
            current_win_count += 1
        else:
            if symbol in ['@', '#', '$', '^']:
                number_of_repeat = current_win_count
                winning_symbol = current_win_symbol
                current_win_symbol = symbol
                current_win_count = 1
            else:
                current_win_symbol = ''
                current_win_count = 0
                continue
        if current_win_count > number_of_repeat:
            number_of_repeat = current_win_count
            winning_symbol = current_win_symbol
    return winning_symbol, number_of_repeat


tickets = input().split()
tickets_list = (''.join(tickets)).split(',')

for ticket in tickets_list:
    left_win_symbol = ''
    right_win_symbol = ''
    left_repeat = 0
    right_repeat = 0

    if check_length(ticket):
        # Checking left half ot ticket
        left_win_symbol, left_repeat = check_half_ticket(ticket[:10])
        if left_repeat < 6:
            print(f'ticket "{ticket}" - no match')
        else:
            # Checking right half ot ticket
            right_win_symbol, right_repeat = check_half_ticket(ticket[10:])
            if right_repeat < 6 or right_win_symbol != left_win_symbol:
                print(f'ticket "{ticket}" - no match')
            else:
                # Case when, we have win ticket
                if left_win_symbol == right_win_symbol:
                    win_symbol = left_win_symbol
                    count_repeat = min(left_repeat, right_repeat)
                    # Checking for jackpot!
                    if count_repeat < 10:
                        print(f'ticket "{ticket}" - {count_repeat}{win_symbol}')
                    else:
                        print(f'ticket "{ticket}" - {count_repeat}{win_symbol} Jackpot!')
    else:
        print("invalid ticket")
