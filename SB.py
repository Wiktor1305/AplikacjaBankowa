import socket as s
import yaml

def logowanie(login): #główna funkcja obsługująca program

    print(f"[{address[0]}:{address[1]}]> Nazwa uzytkownika: {login}")

    msg = f"Witaj na serwerze, {login}!".encode("utf8") #powitanie
    client_socket.send(msg)

    haslo = client_socket.recv(BUFFER).decode("utf8")

    if haslo == x: #instrukcja if, podano prawidłowe hasło
        print(f"[{address[0]}:{address[1]}]> Podano prawidlowe haslo")

        msg2 = f"Poprawnie zalogowales sie do aplikacji".encode("utf8")
        client_socket.send(msg2)

    else: #instrukcja if, podano nieprawidłowe hasło
        print(f"[{address[0]}:{address[1]}]> Podano nieprawidlowe haslo")

        msg3 = f"Podano zle haslo! Masz jeszcze jedna probe.".encode("utf8")
        client_socket.send(msg3)

        haslo = client_socket.recv(BUFFER).decode("utf8")

        if haslo == x: #instrukcja if, druga próba podania dobrego hasła
            print(f"[{address[0]}:{address[1]}]> Podano prawidlowe haslo")

            msg2 = f"Poprawnie zalogowales sie do aplikacji".encode("utf8")
            client_socket.send(msg2)

        else: #instrukcja if, podano nieprawidłowe hasło po raz drugi
            print(f"[{address[0]}:{address[1]}]> Podano nieprawidlowe haslo")

            msg3 = f"Podano zle haslo!".encode("utf8")
            client_socket.send(msg3)

    wybor = client_socket.recv(BUFFER).decode("utf8")

    if wybor == "1": #opcja pierwsza z menu, przelew środków na inne konto
        print("Wybrano przelew srodkow na inne konto.")
        msg = f"Wybrano przelew srodkow na inne konto.".encode("utf8")
        client_socket.send(msg)
        przelew = client_socket.recv(BUFFER).decode("utf8")

        with open(f"{l}.yml", "r") as q: #pobranie danych klienta z pliku YAML
            y = yaml.safe_load(q)
            imie = y[0]
            nazwisko = y[1]
            pesel = y[2]
            nr_konta = y[3]
            login = y[4]
            haslo = y[5]
            saldo = y[6]["saldo"]
            print(f"Saldo wynosi: {saldo}")

            if int(przelew)>int(saldo): #zapobiegnięcie sytuacji przelania środków pomimo jego braku
                print(f"Nie wystarczjaca ilosc srodkow")
                msg2 = f"Saldno wynosi: {saldo}. Nie wystarczajaca ilosc srodkow.".encode("utf8")
                client_socket.send(msg2)
                return

            else: #wybór konta na jakie chcemy przelać środki
                msg3 = f"Na jaki numer konta chcesz przelac srodki?".encode("utf8")
                client_socket.send(msg3)

                nr_konta = client_socket.recv(BUFFER).decode("utf8")

                def przelew_srodkow(nazwa): #funkcja przelew środków
                    with open(f"{nazwa}.yml", "r") as q: #pobranie danych klienta z pliku YAML
                        y = yaml.safe_load(q)
                        imie = y[0]
                        nazwisko = y[1]
                        pesel = y[2]
                        nr_konta = y[3]
                        login = y[4]
                        haslo = y[5]
                        saldo = y[6]["saldo"]
                        print(f"Saldo odbierajacego srodki wynosi: {saldo}")

                    with open(f"{nazwa}.yml", "w") as outfile: #edycja danych klienta w pliku YAML
                        z = saldo + int(przelew)
                        obiekt = {"saldo": z}
                        v = imie, nazwisko, pesel, nr_konta, login, haslo, obiekt
                        yaml.safe_dump(v, outfile)
                    outfile.close()
                    print(f"Srodki przelano pomyslnie.")

                def odjecie_srodkow(): #funkcja odjęcia przelanych środków nadawcy
                    with open(f"{l}.yml", "r") as w: #pobranie danych klienta z pliku YAML
                        d = yaml.safe_load(w)
                        imie = d[0]
                        nazwisko = d[1]
                        pesel = d[2]
                        nr_konta = d[3]
                        login = d[4]
                        haslo = d[5]
                        saldo = d[6]["saldo"]
                        print(f"Saldo wynosi: {saldo}")

                    with open(f"{l}.yml", "w") as outfile: #edycja danych klienta w pliku YAML
                        z = saldo - int(przelew)
                        obiekt = {"saldo": z}
                        v = imie, nazwisko, pesel, nr_konta, login, haslo, obiekt
                        yaml.safe_dump(v, outfile)
                        outfile.close()
                        print("Srodki odebrane nadawcy pomyslnie.")

                def przelano_srodki(nazwa): #funkcja przelano środki, pobiera dane z plików YAML nadawcy i odbiorcy oraz pokazuje zaktualizowane salda
                    with open(f"{l}.yml", "r") as q: #pobranie danych klienta z pliku YAML
                        y = yaml.safe_load(q)
                        saldo = y[6]["saldo"]
                        print(f"Saldo nadawcy wynosi: {saldo}")

                    with open(f"{nazwa}.yml", "r") as q: #pobranie danych klienta z pliku YAML
                        y = yaml.safe_load(q)
                        saldo2 = y[6]["saldo"]
                        print(f"Saldo odbiorcy wynosi: {saldo2}")

                    msg4 = f"Przelano pomyslnie srodki. Saldo nadawcy wynosi: {saldo} zl, a saldo odbiorcy: {saldo2} zl.".encode("utf8")
                    client_socket.send(msg4) #wysłanie wiadomości do terminalu klienta w której treści program przedstawia salda nadawcy i odbiorcy

                if nr_konta == "3042": #numer konta przypisany do użytkownika Kowalski
                    przelew_srodkow("Mati")
                    odjecie_srodkow()
                    przelano_srodki("Mati") #wykonanie trzech funkcji

                elif nr_konta == "2013": #numer konta przypisany do użytkownika Nowakowski
                    przelew_srodkow("Jasiu")
                    odjecie_srodkow()
                    przelano_srodki("Jasiu") #wykonanie trzech funkcji

                elif nr_konta == "1856": #numer konta przypisany do użytkownika Matusiak
                    przelew_srodkow("Monia")
                    odjecie_srodkow()
                    przelano_srodki("Monia") #wykonanie trzech funkcji

                elif nr_konta == "5143": #numer konta przypisany do użytkownika Chodakowska
                    przelew_srodkow("Jusia")
                    odjecie_srodkow()
                    przelano_srodki("Jusia") #wykonanie trzech funkcji

                else: #błędny numer konta
                    msg5 = f"Bledny numer konta!".encode("utf8")
                    client_socket.send(msg5)


    elif wybor == "2": #opcja druga z menu, wypłacenie środków
        print("Wybrano wyplac srodki.")
        msg = f"Wpisz kwote jaka chcesz wyplacic.".encode("utf8")
        client_socket.send(msg)
        wyplata = client_socket.recv(BUFFER).decode("utf8")

        with open(f"{l}.yml", "r") as q: #pobranie danych klienta z pliku YAML
            y = yaml.safe_load(q)
            imie = y[0]
            nazwisko = y[1]
            pesel = y[2]
            nr_konta = y[3]
            login = y[4]
            haslo = y[5]
            saldo = y[6]["saldo"]
            print(f"Saldo wynosi: {saldo}")

            if int(wyplata)>int(saldo): #zapobiegnięcie sytuacji wypłacenia środków pomimo ich braku
                print(f"Nie wystarczjaca ilosc srodkow")
                msg2 = f"Saldno wynosi: {saldo}. Nie wystarczajaca ilosc srodkow.".encode("utf8")
                client_socket.send(msg2)
                return

            else: #instrukcja if odejmująca wypłacone środki od salda użytkownika
                with open(f"{l}.yml", "w") as outfile:
                    z = saldo - int(wyplata)
                    obiekt = {"saldo": z}
                    v = imie, nazwisko, pesel, nr_konta, login, haslo, obiekt
                    yaml.safe_dump(v, outfile)
                outfile.close()

                print(f"Saldo po dokonaniu wyplaty wynosi: {z} zl")
                msg2 = f"Wyplacono {wyplata} zl. Saldo po dokonaniu wyplaty wynosi: {z} zl".encode("utf8")
                client_socket.send(msg2)


    elif wybor == "3": #opcja trzecia z menu, wypłata środków
        print("Wybrano dokonaj wplaty.")
        msg = f"Wplata".encode("utf8")
        client_socket.send(msg)
        kwota = client_socket.recv(BUFFER).decode("utf8")

        with open(f"{l}.yml", "r") as q: #pobranie danych klienta z pliku YAML
            y = yaml.safe_load(q)
            imie = y[0]
            nazwisko = y[1]
            pesel = y[2]
            nr_konta = y[3]
            login = y[4]
            haslo = y[5]
            saldo = y[6]["saldo"]
            print(f"Saldo wynosi: {saldo}")

        with open(f"{l}.yml", "w") as outfile: #edycja danych klienta w pliku YAML
            z = saldo + int(kwota)
            obiekt = {"saldo": z}
            v = imie, nazwisko, pesel, nr_konta, login, haslo, obiekt
            yaml.safe_dump(v, outfile)
        outfile.close()

        print(f"Saldo po dokonaniu wplaty wynosi: {z} zl")
        msg2 = f"Saldo po dokonaniu wplaty wynosi: {z} zl".encode("utf8")
        client_socket.send(msg2)



    elif wybor == "4": #opcja czwarta z menu, sprawdzenie stanu konta
        print("Wybrano sprawdz stan konta.")
        msg = f"Stan konta".encode("utf8")
        client_socket.send(msg)
        client_socket.recv(BUFFER).decode("utf8")

        with open(f"{login}.yml", "r") as s: #pobranie danych klienta z pliku YAML
            y = yaml.safe_load(s)
            saldo = y[6]["saldo"]
            print(saldo)

        msg2 = f"Twoj stan konta wynosi: {saldo} zl".encode("utf8")
        client_socket.send(msg2)


HOST = "192.168.1.17" #protokół IPv4
PORT = 35000 #port

BUFFER = 1024 #bufor

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2) #składowe python socket

while True: #pętla while
    client_socket, address = server_socket.accept()

    print(f"Uzyskano polaczenie od {address} | lub {address[0]}:{address[1]}")

    login = client_socket.recv(BUFFER).decode("utf8")

    if login == "Mati": #użytkownik Kowalski, haslo, login i numer konta, załączenie funkcji głównej
        x = "1234"
        l = "Mati"
        nr = "3042"
        logowanie("Mati")


    elif login == "Jasiu": #użytkownik Nowakowski, haslo, login i numer konta, załączenie funkcji głównej
        x = "4321"
        l = "Jasiu"
        nr = "2013"
        logowanie("Jasiu")


    elif login == "Monia": #użytkownik Matusiak, haslo, login i numer konta, załączenie funkcji głównej
        x = "1111"
        l = "Monia"
        nr = "1856"
        logowanie("Monia")


    elif login == "Jusia": #użytkownik Chodakowska, haslo, login i numer konta, załączenie funkcji głównej
        x = "2222"
        l = "Jusia"
        nr = "5143"
        logowanie("Jusia")


    else:
        print(f"[{address[0]}:{address[1]}]> Nie ma takiego uzytkownika!") #intrukcje w razie wpisania złego użytkownika

        msg = f"Nie ma takiego uzytkownika".encode("utf8")
        client_socket.send(msg)

