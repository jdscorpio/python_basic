number = float(input("Podaj liczbę: "))

if number >= 2 and number <= 3:
    print("należy")
else:
    print("nie należy")

a, b, c = map(int, input("Podaj boki trójkąta: ").split())

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Trójkąt prostokątny")
else:
    print("Nie jest to trójkąt prostokątny")

