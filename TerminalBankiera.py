import random

lista_a = []
# Dodawanie klientów
decyzja = input("Czy chcesz dodać klienta? Wpisz Tak/Nie")

if decyzja == "Tak":
    print("Dobrze a więc zacznijmy")
    dimie = input("Wpisz imię:")
    lista_a.append(dimie)
    dnazwisko = input("Wpisz nazwisko:")
    lista_a.append(dnazwisko)
    dpesel = input("Wpisz pesel:")
    lista_a.append(dpesel)
    dnrkonta = random.randint(1000, 9999)
    print("Oto unikalny numer konta stworzony dla klienta: " + str(dnrkonta))
    lista_a.append(dnrkonta)
    print(lista_a)
    f = open("dane1.txt", "a")
    f.write(dimie)



elif decyzja == "Nie":
    print("Dobrze a więc miłego dnia!")
