class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.sequence:
            raise StopIteration
        if self.i == self.number:
            raise StopIteration
        idx = self.i % len(self.sequence)
        self.i += 1
        return self.sequence[idx]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
