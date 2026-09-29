text = input("Please, enter text: ")

try:
    times = int(input("Please, enter a number: "))

    print(text * times)

except ValueError:
    print("Variable times must be an integer")
