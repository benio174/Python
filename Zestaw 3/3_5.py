def draw_measure(length):
    measure_line = '|....' * length + '|'

    number_line = ''
    for i in range(0, length + 1):
        if i >= 9 and i <= 99:
            number_line += str(i) + '   '
        else:
            number_line += str(i) + '    '
    print(measure_line)
    print(number_line)


try:
    length = int(input("Podaj dlugosc miarki: "))
    draw_measure(length)
except ValueError:
    print("Podano zla wartosc.")