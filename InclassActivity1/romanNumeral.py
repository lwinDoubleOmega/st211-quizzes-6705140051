class convertfromRoman:
    def __init__(self, roman):
        self.roman = roman
        self.roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def convert(self):
        total = 0
        prev_value = 0

        for char in reversed(self.roman):
            value = self.roman_numerals[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total
