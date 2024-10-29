L = [3, 5, 4] ; L = L.sort()
#L.sort() zwraca None a nie posortowana liste przez co L równa sie none

x, y = 1, 2, 3
#ten kod jest niepoprawny ponieważ po prawej stronie są trzy wartości a po lewej tylko dwie zmienne

X = 1, 2, 3 ; X[1] = 4
#X jest krotką co oznacza że nie można już zmienić wartości w X po ich przypisaniu

X = [1, 2, 3] ; X[3] = 4
#W liście X mamy trzy wartości indeksowane od 0 czyli: 0, 1, 2. Index 3 wykracza poza listę

X = "abc" ; X.append("d")
#X jest typu string a w string nie ma metody append()

L = list(map(pow, range(8)))
#Funkcja pow wymaga dwóch argumentów - podstawy i wykładnika, której tu nie podano
