def find(s1, s2):

    set1 = set(s1)
    set2 = set(s2)

    common = list(set1.intersection(set2))
    all = list(set1.union(set2))

    return(common, all)

seq1 = [1, 2, 3, 6, 7]
seq2 = [1, 3, 5, 6, 8]

seq3 = 'ascds'
seq4 = 'asvsd'

common, all = find(seq1, seq2)
print("Elementy wspolne: ", common)
print("Wszystkie elementy: ", all)

common, all = find(seq3, seq4)
print("Elementy wspolne: ", common)
print("Wszystkie elementy: ", all)