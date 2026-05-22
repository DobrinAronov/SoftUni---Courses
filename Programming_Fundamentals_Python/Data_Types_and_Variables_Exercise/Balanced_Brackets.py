number_of_lines = int(input())

count_open_brackets = 0
count_close_brackets = 0
previous_expression = ''

is_balanced = True

for line in range(number_of_lines):
    expression = input()
# Checking for nested parentheses that are not valid!
    if  expression == '(':
        if  previous_expression == '(':
            is_balanced = False
            break
        count_open_brackets += 1
# Condition: there can be ')' only if the previous expression is '('
    elif    expression == ')':
        if previous_expression == '(':
            count_close_brackets += 1
        else:
            is_balanced = False
            break

    else:
        continue
# overwrite previous_expression only in cases: '(' or ')'
    previous_expression = expression

else:
    if  count_open_brackets != count_close_brackets:
        is_balanced = False

if  is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")