flatten_list = reversed([el.split() for el in input().split('|')])
[print(el, end=' ') for sub_list in flatten_list for el in sub_list]