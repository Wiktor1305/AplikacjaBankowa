import socket as s

class Klient:
    def __init__(self, imie, nazwisko, pesel, nrkonta, login, haslo):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.nrkonta = nrkonta
        self.login = login
        self.haslo = haslo

    def przedstawSie(self, powitanie = "Cześć"):
        return powitanie + ", mam na imię " + self.imie + ", mam " + self.pesel + " lat."

#Dane klientów
klient1 = Klient("Mateusz", "Kowalski", "00241508461", "3042", "Mati", "1234")
klient2 = Klient("Jan", "Nowakowski", "00231678451", "2013", "Jasiu", "4321")
klient3 = Klient("Monika", "Matusiak", "00221815631", "1856", "Monia", "0000")
klient4 = Klient("Justyna", "Chodakowska", "00212167451", "5143", "Jusia", "0001")


#Funkcja:
def logowanie(login):

    print(f"[{address[0]}:{address[1]}]> Nazwa uzytkownika: {login}")

    msg = f"Witaj na serwerze, {login}!".encode("utf8")
    client_socket.send(msg)

    haslo = client_socket.recv(BUFFER).decode("utf8")

    if haslo == x:
        print(f"[{address[0]}:{address[1]}]> Podano prawidlowe haslo")

        msg2 = f"Poprawnie zalogowales sie do aplikacji".encode("utf8")
        client_socket.send(msg2)

    else:
        print(f"[{address[0]}:{address[1]}]> Podano nieprawidlowe haslo")

        msg3 = f"Podano zle haslo!".encode("utf8")
        client_socket.send(msg3)


HOST = "192.168.1.17"
PORT = 33000

BUFFER = 1024

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2)

while True:
    client_socket, address = server_socket.accept()

    print(f"Uzyskano polaczenie od {address} | lub {address[0]}:{address[1]}")

    login = client_socket.recv(BUFFER).decode("utf8")

    if login == "Mati":
        x = "1234"
        logowanie("Mati")


    elif login == "Jasiu":
        x = "4321"
        logowanie("Jasiu")


    elif login == "Monia":
        x = "0000"
        logowanie("Monia")


    elif login == "Jusia":
        x = "0001"
        logowanie("Jusia")


    else:
        print(f"[{address[0]}:{address[1]}]> Nie ma takiego uzytkownika!")

        msg = f"Nie ma takiego uzytkownika".encode("utf8")
        client_socket.send(msg)
