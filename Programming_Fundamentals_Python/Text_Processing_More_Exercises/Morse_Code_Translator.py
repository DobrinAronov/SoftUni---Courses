import time

import winsound


def morse_code_translator(list_with_morse_codes: list, morse_alphabet: dict) -> str:
    output_message = ''

    for morse_letter in list_with_morse_codes:
        for sign in morse_letter:
            if sign not in ('.', '-', '|', ' '):
                return "Това не е морзов код !!!"
        if morse_letter == '|':
            output_message += ' '
        else:
            for letter, code in morse_alphabet.items():
                if morse_letter == code:
                    output_message += letter
    return output_message


def message_morse_coding(text_for_coding: str, morse_alphabet: dict) -> str:
    output_morse_code = ''

    for symbol in text_for_coding:
        if symbol == ' ':
            output_morse_code += '| '
        else:
            if symbol.upper() in morse_alphabet:
                output_morse_code += morse_alphabet[symbol.upper()] + ' '
    return output_morse_code


def sound(morse_code: str):
    message_for_send = ''
    # Adding the "p" symbol between Morse code characters into one letter.
    for idx in range(len(morse_code)):
        symbol = morse_code[idx]
        if (idx + 1) < len(morse_code):
            next_symbol = morse_code[idx + 1]
            if next_symbol != ' ' or next_symbol != '|':
                message_for_send += symbol + 'p'
            else:
                message_for_send += symbol

    for symbol in message_for_send:
        if symbol == '.':
            # point - frequency 600 Hz, duration 100 mS
            winsound.Beep(600, 100)
        elif symbol == '-':
            # dash - frequency 600 Hz, duration 300 mS
            winsound.Beep(600, 300)
        # I replace the "p" symbol with a space
        # to separate the Morse code characters into one letter.
        elif symbol == 'p':
            # duration pause between symbols 100 mS
            time.sleep(0.1)
        elif symbol == ' ':
            # duration pause between letters 300 mS
            time.sleep(0.3)
        elif symbol == '|':
            # duration pause between words 700 mS
            time.sleep(0.7)


morse_code_alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                       'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
                       'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '—–',
                       '1': '.—-', '2': '..—', '3': '...–', '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.'
                       }

command = input("\nМоля, изберете действие:\n"
                "'C' за кодиране на съобщение\n"
                "'D' за декодиране на съобщение\n"
                "За изход от програмата въведете End\n").lower()

while command != "end":

    if command == 'd':
        morse_code_list = input("Моля, въведете морзов код: ").split()
        text_message = morse_code_translator(morse_code_list, morse_code_alphabet)
        print(f"Декодирано съобщение:\n{text_message}")

    elif command == 'c':
        text = input("Моля, въведете текстово съобщение на латиница!\n")
        code_message = message_morse_coding(text, morse_code_alphabet)
        print(f"Морзов код:\n{code_message}\n")
        # If the user wants to hear the message
        sound_command = input("Моля, въведете Y ако искате да чуете съобщението\n"
                              "или произволен клавиш за да продължите\n"
                              "Потвърдете с Enter: ").lower()
        if sound_command == 'y':
            sound(code_message)

    else:
        print("Грешна команда!")

    command = input("\nМоля, изберете действие:\n"
                    "'C' за кодиране на съобщение\n"
                    "'D' за декодиране на съобщение\n"
                    "За изход от програмата въведете End\n").lower()
