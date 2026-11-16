class dictionary_iter:
    def __init__(self, dict_iterable: dict):
        self.dict_iterable = tuple(dict_iterable.items())
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.dict_iterable):
            value = self.dict_iterable[self.i]
            self.i += 1
            return value
        raise StopIteration



result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
