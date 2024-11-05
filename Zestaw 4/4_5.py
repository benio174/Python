def reverse_ite(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return L

def reverse_rek(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        reverse_rek(L, left + 1, right - 1)
    return L

L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
M = reverse_ite(L1, 2, 6)
print(M)

L2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = reverse_rek(L2, 2, 6)
print(N)