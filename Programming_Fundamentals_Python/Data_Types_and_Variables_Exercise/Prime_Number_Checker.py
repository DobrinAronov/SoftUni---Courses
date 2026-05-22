checking_number = int(input())

is_prime = True
# Checking for prime number
for number in range(2, int(checking_number ** 0.5) + 1):
    if  checking_number % number == 0:
        is_prime = False
        break

if is_prime:
    print(True)
else:
    print(False)