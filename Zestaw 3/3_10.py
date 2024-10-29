def roman2int(roman):
    roman_to_arabic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman):
        value = roman_to_arabic[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

print(roman2int("II"))
print(roman2int("IV"))
print(roman2int("IX"))
print(roman2int("LVIII"))
print(roman2int("MCMXCIV"))


roman_to_arabic = {}
roman_symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
arabic_values = [1, 5, 10, 50, 100, 500, 1000]

for symbol, value in zip(roman_symbols, arabic_values):
    roman_to_arabic[symbol] = value

print(roman_to_arabic)


roman_symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
arabic_values = [1, 5, 10, 50, 100, 500, 1000]
roman_to_arabic = dict(zip(roman_symbols, arabic_values))

print(roman_to_arabic)