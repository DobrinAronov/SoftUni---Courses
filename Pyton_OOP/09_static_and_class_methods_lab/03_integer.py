roman_numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if type(float_value) != float:
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, roman_number: str):
        curr_number = 0
        for i in range(len(roman_number)):
            if i < len(roman_number) - 1 and \
                    roman_numerals[roman_number[i]] < roman_numerals[roman_number[i + 1]]:
                curr_number -= roman_numerals[roman_number[i]]
            else:
                curr_number += roman_numerals[roman_number[i]]
        return cls(curr_number)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str) and value.isdigit():
            return cls(int(value))
        return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
