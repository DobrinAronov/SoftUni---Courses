class vowels:
    VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

    def __init__(self, text):
        self.text = text
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self.text):

            letter = self.text[self.idx]
            self.idx += 1

            if letter.lower() in self.VOWELS:
                return letter

        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
