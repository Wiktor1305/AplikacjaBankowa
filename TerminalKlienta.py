import socket as s

HOST = "192.168.1.17"
PORT = 33000

BUFFER = 1024

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((HOST, PORT))

name = input("Twoje imię: ").encode("utf8")

client_socket.send(name)

print(client_socket.recv(BUFFER))
