# import socket as s
#
# HOST = "192.168.1.17"
# PORT = 33000
#
# BUFFER = 1024
#
# server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
# server_socket.bind((HOST, PORT))
# server_socket.listen(2)
#
# while True:
#     client_socket, address = server_socket.accept()
#
#     print(f"Uzyskano połączenie od {address} | lub {address[0]}:{address[1]}")
#
#     name = client_socket.recv(BUFFER).decode("utf8")
#
#     print(f"[{address[0]}:{address[1]}]> Nazwa użytkownika: {name}")
#
#     msg = f"Witaj na serwerze, {name}!".encode("utf8")
#     client_socket.send(msg)
import socket as s

HOST = "192.168.1.17"
PORT = 33000

BUFFER = 1024

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2)

while True:
    client_socket, address = server_socket.accept()

    print(f"Uzyskano połączenie od {address} | lub {address[0]}:{address[1]}")

    login = client_socket.recv(BUFFER).decode("utf8")

    if login == "Mati":

        print(f"[{address[0]}:{address[1]}]> Nazwa użytkownika: {login}")

        msg = f"Witaj na serwerze, {login}!".encode("utf8")
        client_socket.send(msg)

        haslo = client_socket.recv(BUFFER).decode("utf8")

        if haslo == "1234":
            print(f"[{address[0]}:{address[1]}]> Podano prawidłowe hasło")

            msg2 = f"Poprawnie zalogowałeś się do aplikacji".encode("utf8")
            client_socket.send(msg2)

        else:
            print(f"[{address[0]}:{address[1]}]> Podano nieprawidłowe hasło")

            msg3 = f"Podano złe hasło!".encode("utf8")
            client_socket.send(msg3)


    elif login == "Jasiu":

        print(f"[{address[0]}:{address[1]}]> Nazwa użytkownika: {login}")

        msg = f"Witaj na serwerze, {login}!".encode("utf8")
        client_socket.send(msg)

        haslo = client_socket.recv(BUFFER).decode("utf8")

        if haslo == "4321":
            print(f"[{address[0]}:{address[1]}]> Podano prawidłowe hasło")

            msg2 = f"Poprawnie zalogowałeś się do aplikacji".encode("utf8")
            client_socket.send(msg2)

        else:
            print(f"[{address[0]}:{address[1]}]> Podano nieprawidłowe hasło")

            msg3 = f"Podano złe hasło!".encode("utf8")
            client_socket.send(msg3)

    elif login == "Monia":

        print(f"[{address[0]}:{address[1]}]> Nazwa użytkownika: {login}")

        msg = f"Witaj na serwerze, {login}!".encode("utf8")
        client_socket.send(msg)

        haslo = client_socket.recv(BUFFER).decode("utf8")

        if haslo == "0000":
            print(f"[{address[0]}:{address[1]}]> Podano prawidłowe hasło")

            msg2 = f"Poprawnie zalogowałeś się do aplikacji".encode("utf8")
            client_socket.send(msg2)

        else:
            print(f"[{address[0]}:{address[1]}]> Podano nieprawidłowe hasło")

            msg3 = f"Podano złe hasło!".encode("utf8")
            client_socket.send(msg3)

    elif login == "Jusia":

        print(f"[{address[0]}:{address[1]}]> Nazwa użytkownika: {login}")

        msg = f"Witaj na serwerze, {login}!".encode("utf8")
        client_socket.send(msg)

        haslo = client_socket.recv(BUFFER).decode("utf8")

        if haslo == "0001":
            print(f"[{address[0]}:{address[1]}]> Podano prawidłowe hasło")

            msg2 = f"Poprawnie zalogowałeś się do aplikacji".encode("utf8")
            client_socket.send(msg2)

        else:
            print(f"[{address[0]}:{address[1]}]> Podano nieprawidłowe hasło")

            msg3 = f"Podano złe hasło!".encode("utf8")
            client_socket.send(msg3)

    else:
        print(f"[{address[0]}:{address[1]}]> Nie ma takiego użytkownika!")

        msg = f"Nie ma takiego użytkownika".encode("utf8")
        client_socket.send(msg)


