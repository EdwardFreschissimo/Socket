import socket

sServer=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sClient=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sServer.bind(("0.0.0.0",8080))
sServer.listen()
conn, clientAddress = sServer.accept()
sClient.connect(("192.168.10.52", 8080))

while True:

    data = conn.recv(4096)
    print("\nClient" + data.decode())
    if data.decode() == "EXIT":
        break
    else:
        sClient.sendall(data)
        print("Messaggio")

conn.close()
sServer.close()
sClient.close()