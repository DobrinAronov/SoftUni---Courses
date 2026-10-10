class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


MIN_AGE = 18

pin_code, balance, age = map(int, input().split(', '))

while True:
    command = input()

    if command == "End":
        break

    action, money, *args = command.split('#')
    money = int(money)

    if money < 0:
        raise MoneyIsNegativeError('The amount of money cannot be a negative number')

    if action == "Send Money":
        pin = int(args[0])

        if money > balance:
            raise MoneyNotEnoughError('Insufficient funds for the requested transaction')

        if pin != pin_code:
            raise PINCodeError('Invalid PIN code')

        if age < MIN_AGE:
            raise UnderageTransactionError('You must be 18 years or older to perform online transactions')

        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    elif action == "Receive Money":
        amount_of_money = money / 2
        balance += amount_of_money
        print(f"{amount_of_money:.2f} money went straight into the bank account")
