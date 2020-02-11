import socket 
from threading import Thread

BUFFSIZE = 4096
SERVER_IP = "127.0.0.1"
SERVER_PORT = 1234

class ClientThread(Thread):
    def __init__(self,client_ip,client_port):
        Thread.__init__(self)
        self.client_ip
        self-client_port = client_port
        print(f"New Thread started for {client_ip}, {client_port}")

    def run(self):
        while True:
        data = conn.recv(BUFFSIZE)
        print(f"Server received data: {data.decode()}, from {self.client_ip}")
        if data.decode() == 'EXIT':
        conn.send("RECEIVED".decode())  

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(SERVER_IP, SERVER_PORT)
s.listen(5)
lstOfThread = []
print("MultiThreaded")
while True:
    conn, (ip,port)=s.accept()
    thread=ClientThread(ip,port)
    thred.run
