def decipher_message(scr_message: list) -> str:
    output_list = []
    for word in scr_message:
        digit = ''
        other_letters = ''
        for letter in word:
            if letter.isdigit():
                digit += letter
            else:
                other_letters += letter
        decipher_word_first = chr(int(digit)) + other_letters

        # switch second and last letter

        if len(decipher_word_first) > 2:
            decipher_word_second = decipher_word_first[:1] + decipher_word_first[-1] + \
                                   decipher_word_first[2:-1] + decipher_word_first[1]
            output_list.append(decipher_word_second)
        else:
            output_list.append(decipher_word_first)

    return ' '.join(output_list)


secret_message = input().split()

print(decipher_message(secret_message))
