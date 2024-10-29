def sum_of_sequences(s):
    sums = [sum(seq) for seq in s]
    return sums

L = [[],[4],(1,2),[3,4],(5,6,7)]

sums = sum_of_sequences(L)

print(sums)