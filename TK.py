import socket as s

HOST = "192.168.1.17"
PORT = 33000

BUFFER = 1024

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:

    print(f"Witaj w Banku Maroko!")

    login = input("Wpisz swoj login: ").encode("utf8")

    client_socket.send(login)

    zwrot = client_socket.recv(BUFFER).decode("utf8")

    print(zwrot)

    if zwrot == "Nie ma takiego uzytkownika":
        break

    else:

        haslo = input("Podaj swoje haslo:").encode("utf8")

        client_socket.send(haslo)

        # print(client_socket.recv(BUFFER))

        proba2 = client_socket.recv(BUFFER).decode("utf8")

        print(proba2)

        if proba2 == "Podano zle haslo! Masz jeszcze jedna probe.":

            haslo = input("Podaj swoje haslo:").encode("utf8")

            client_socket.send(haslo)

            print(client_socket.recv(BUFFER))

        break
