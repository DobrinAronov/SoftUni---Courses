def morse_code_translator(word_list: list, morse_codes: dict) -> str:
    output_message = ''

    for morse_letter in word_list:
        if morse_letter == '|':
            output_message += ' '
        else:
            for letter, code in morse_codes.items():
                if morse_letter == code:
                    output_message += letter
                    break
    return output_message


morse_code_alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                       'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
                       'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
                       }

morse_code_list = input().split()

print(morse_code_translator(morse_code_list, morse_code_alphabet))
