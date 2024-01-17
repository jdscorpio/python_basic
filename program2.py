# == !=
number = int(input("Podaj liczbę: "))

if number % 2 == 0:
    print("parzysta")
else:
    print("nieparzysta")

name = input("Podaj imie: ")
if name != "Jarek":
    print("nie ma dziś obiadu")
else:
    print("obiad!")
