def draw(a, b):

    side1 = '+----' * b + '+'
    side2 = '|    ' * b + '|'
    while a > 0:
        print(side1)
        print(side2)
        a -= 1
    print(side1)

try:
    width = int(input("Podaj szerokosc prostokata: "))
    length = int(input("Podaj dlugosc prostokata: "))
    draw(width, length)
except ValueError:
    print("Podano zla wartosc")
