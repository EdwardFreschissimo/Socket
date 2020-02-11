import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP_SERVER = input("Indirizzo server: ")
PORT = int(input("Porta"))
s.connect((Ip_SERVER, PORT))

while True:
    op=s.recv(4096).decode()
    if op=='exit':
        break
    eval(op)
    s.send(op.encode())

s.close()
