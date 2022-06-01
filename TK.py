import socket as s

HOST = "192.168.1.17" #protokół IPv4
PORT = 35000 #port

BUFFER = 1024 #bufor

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((HOST, PORT)) #składowe python socket

while True: #pętla while zawierająca program terminalu klienta

    print(f"Witaj w Banku Maroko!") #powitanie

    login = input("Wpisz swoj login: ").encode("utf8")

    client_socket.send(login)

    zwrot = client_socket.recv(BUFFER).decode("utf8")

    print(zwrot)

    if zwrot == "Nie ma takiego uzytkownika": #instrukcja if i zatrzymanie programu
        break

    else: #instrukcja if i żądanie hasła

        haslo = input("Podaj swoje haslo:").encode("utf8")

        client_socket.send(haslo)

        proba2 = client_socket.recv(BUFFER).decode("utf8")

        print(proba2)

        if proba2 == "Podano zle haslo! Masz jeszcze jedna probe.": #instrukcja if, próba druga podania hasła

            haslo = input("Podaj swoje haslo:").encode("utf8")

            client_socket.send(haslo)

            odpowiedz = client_socket.recv(BUFFER).decode("utf8")

            print(odpowiedz)

            if odpowiedz == "Podano zle haslo!": #instrukcja if, podano nieprawidłowe hasło po raz drugi
                break



        print("1. Przelew srodkow na inne konto.")
        print("2. Wyplac srodki.")
        print("3. Dokonaj wplaty.")
        print("4. Sprawdz stan konta.") #menu i cztery opcje

        wybor = input("Jaka akcje chcesz przeprowadzic? Wpisz cyfre:").encode("utf8")

        client_socket.send(wybor)

        wybor2 = client_socket.recv(BUFFER).decode("utf8")

        if wybor2 == "Wybrano przelew srodkow na inne konto.": #opcja pierwsza z menu, przelew środków na inne konto
            przelew = input("Wpisz kwote jaka chcesz przelac:").encode("utf8")
            client_socket.send(przelew)

            dostepnosc = client_socket.recv(BUFFER).decode("utf8")
            print(dostepnosc)

            if dostepnosc == "Na jaki numer konta chcesz przelac srodki?": #instrukcja if, podanie numeru konta odbiorcy
                nr_konta = input("Wpisz numer konta docelowego:").encode("utf8")
                client_socket.send(nr_konta)
                print(client_socket.recv(BUFFER).decode("utf8"))


            else:
                break

        elif wybor2 == "Wpisz kwote jaka chcesz wyplacic.": #opcja druga z menu, wypłacenie środków
            wyplata = input("Wpisz kwote jaka chcesz wyplacic z konta:").encode("utf8")
            client_socket.send(wyplata)

            print(client_socket.recv(BUFFER).decode("utf8"))

        elif wybor2 == "Wplata": #opcja trzecia z menu, wypłata środków
            wplata = input("Wpisz kwote jaka chcesz wplacic na konto:").encode("utf8")
            client_socket.send(wplata)

            print(client_socket.recv(BUFFER).decode("utf8"))



        elif wybor2 == "Stan konta": #opcja czwarta z menu, sprawdzenie stanu konta
            client_socket.send("stan konta".encode("utf8"))
            print(client_socket.recv(BUFFER).decode("utf8"))


        break
