line = "abc\nhj\te\nxy"

new_line = line.split()

abc_sort = sorted(new_line)
print("Wyraz line posortowany alfabetycznie: ", abc_sort)

length_sort = sorted(new_line, key = len, reverse = True)
print("Wyraz line posortowany pod wzgledem dlugosci: ", length_sort)