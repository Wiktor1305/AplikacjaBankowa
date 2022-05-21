import socket as s

HOST = "192.168.1.17"
PORT = 33000

BUFFER = 1024

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print(f"Witaj w Banku Maroko!")

login = input("Wpisz swoj login: ").encode("utf8")

client_socket.send(login)

print(client_socket.recv(BUFFER))

# zwrot = BUFFER
#
# def user(zwrot):
#
#     if zwrot == "Nie ma takiego użytkownika":
#         return
#
#     else:

haslo = input("Podaj swoje haslo:").encode("utf8")

client_socket.send(haslo)

print(client_socket.recv(BUFFER))
