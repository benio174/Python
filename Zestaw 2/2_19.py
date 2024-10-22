L = [1, 23, 426, 5, 43, 2, 748]

new = ''.join([str(num).zfill(3) for num in L])

print(new)