line = "ab\nc\tef\nxy"

first_letters = ''.join([word[0] for word in line.split()])

print("Napis stworzony z pierwszych znakow z napisu line:", first_letters)

last_letters =''.join([word[-1] for word in line.split()])

print("Napis stworzony z ostatnich znakow z napisu line:", last_letters)