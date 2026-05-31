def loading_bar(num: int) ->list:

    load = int(num / 10)
    rest = 10 - load
    left_part = ['%' for i in range(load)]
    right_part = ['.' for j in range(rest)]
    output_list = left_part + right_part
    return output_list

number = int(input())

if  number != 100:
    print(f"{number}% [{''.join(loading_bar(number))}]")
    print("Still loading...")
else:
    print("100% Complete!")
    print(f"[{''.join(loading_bar(number))}]")