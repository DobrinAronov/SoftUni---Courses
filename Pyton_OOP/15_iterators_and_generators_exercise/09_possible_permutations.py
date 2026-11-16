from itertools import permutations


def possible_permutations(seq):
    yield from (list(p) for p in permutations(seq))


[print(n) for n in possible_permutations([1, 2, 3])]
