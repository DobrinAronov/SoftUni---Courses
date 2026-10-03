numbers_file = None

try:
    numbers_file = open('numbers_file.txt', "r")
    total_sum = sum(int(num) for num in numbers_file if num.strip())
    print(total_sum)

except FileNotFoundError:
    print("File not found!")

finally:
    if numbers_file is not None:
        numbers_file.close()
