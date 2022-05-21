HOST = "192.168.1.17"
PORT = 33000

BUFFER = 1024

def logowanie(login):

    print(f"[{address[0]}:{address[1]}]> Nazwa użytkownika: {login}")

    msg = f"Witaj na serwerze, {login}!".encode("utf8")
    client_socket.send(msg)

    haslo = client_socket.recv(BUFFER).decode("utf8")

    if haslo == x:
        print(f"[{address[0]}:{address[1]}]> Podano prawidłowe hasło")

        msg2 = f"Poprawnie zalogowałeś się do aplikacji".encode("utf8")
        client_socket.send(msg2)

    else:
        print(f"[{address[0]}:{address[1]}]> Podano nieprawidłowe hasło")

        msg3 = f"Podano złe hasło!".encode("utf8")
        client_socket.send(msg3)




