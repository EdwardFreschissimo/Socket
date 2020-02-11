import socket as sck 

HOST = "127.0.0.1"
PORT = 8080

s = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
s.bind((HOST,PORT))

while True:
    data,address = s.recvfrom(4096)
    print("ricevuto --> " + str(data.decode()) + " da " + str(address))

    if(str(data.decode()) == "stop"):
        break

    #text = input("inserisci risposta: ")
    #s.sendto(text.encode(),address)
    
s.close()
print("chiusura server")