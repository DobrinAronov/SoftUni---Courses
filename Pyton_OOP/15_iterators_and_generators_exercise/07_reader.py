def read_next(*collections):
    for sequence in collections:
        yield from sequence


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
