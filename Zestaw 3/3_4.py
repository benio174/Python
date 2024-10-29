while True:
    number = input("Podaj liczbe rzeczywista: ")
    if number.lower() == 'stop':
        print("Zatrzymano program")
        break
    try:
        x = float(number)
        print(f"Liczba: {x}")
        print(f"Trzecia potega: {x**3}")
    except ValueError:
        print("Podano zla wartosc")
