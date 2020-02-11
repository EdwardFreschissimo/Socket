import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",5432))
s.listen()
conn, clientAddress = s.accept()
print("Connesso con ", conn)

while True:

    data = conn.recv(4096).decode()
    print("/n>client %s: %s" %(clientAddress, data))
    strToSend = input(">")
    conn.sendall(strToSend.encode())
    if strToSend=='0':
        break

conn.close()
s.close()