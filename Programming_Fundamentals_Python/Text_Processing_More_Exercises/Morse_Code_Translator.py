def morse_code_translator(word_list: list) -> str:
    output_message = ''
    morse_code_letters = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                          'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                          'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
                          'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
                          }

    for morse_letter in word_list:
        if morse_letter == '|':
            output_message += ' '
        else:
            for letter, code in morse_code_letters.items():
                if morse_letter == code:
                    output_message += letter
    return output_message


morse_code_list = input().split()

print(morse_code_translator(morse_code_list))
