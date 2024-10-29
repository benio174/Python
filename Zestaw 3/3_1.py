x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

#Kod jest poprawny składowo, natomiast nie ma potrzeby używania znaku ";" na końcu linii. Również nawias w linijce drugiej nie jest
#konieczny

for i in "axby": if ord(i) < 100: print (i)

#Ten kod jest niepoprawny ponieważ brakuje wcięcia po instruckji if oraz for

for i in "axby": print (ord(i) if ord(i) < 100 else i)

#Ten kod jest poprawny i działa prawidłowo
