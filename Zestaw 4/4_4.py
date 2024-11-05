def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(2, n + 1):
            a, b = b, a + b

    return b

F = fibonacci(7)
print(F)
