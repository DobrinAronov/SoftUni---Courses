from math import log

def calculate_logarithm(num:int, base)->float:
    try:
        return log(num, int(base))

    except ValueError:
        return log(num)