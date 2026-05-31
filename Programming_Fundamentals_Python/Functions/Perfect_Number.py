def perfect_number(num: int) ->bool:
    divisors = []
    for number in range(1, num):
        if num % number == 0:
            divisors.append(number)
    if sum(divisors) == num:
        return True
    return False

checking_number = int(input())

result = perfect_number(checking_number)

if result:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")