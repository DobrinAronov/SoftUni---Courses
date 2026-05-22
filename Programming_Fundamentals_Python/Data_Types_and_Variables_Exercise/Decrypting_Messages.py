key = int(input())
number_of_lines = int(input())

decrypting_massage = ''

for number in range(number_of_lines):
    letter = input()
    decrypting_massage += chr(key + ord(letter))

print(decrypting_massage)