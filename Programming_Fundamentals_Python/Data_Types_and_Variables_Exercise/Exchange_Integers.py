a = int(input())
b = int(input())

print(f"Before:\na = {a}\nb = {b}")

temporary_variable = a
a = b
b = temporary_variable

print(f"After:\na = {a}\nb = {b}")