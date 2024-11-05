def make_ruler(n):
    number_line = ''
    for i in range(0, n + 1):
        if i >= 9 and i <= 99:
            number_line += str(i) + '   '
        else:
            number_line += str(i) + '    '

    ruler = '|....' * n + '|\n' + number_line
    return ruler

ruler = make_ruler(12)
print(ruler)

def make_grid(rows, cols):
    side = '+----' * cols + '+\n' + '|    ' * cols + '|\n'
    square = ''
    while rows > 0:
        square += side
        rows -= 1
    square += '+----' * cols + '+'
    return square

square = make_grid(2, 4)
print(square)