import socket as sck 

HOST = "Gesù Super Sayan"
PORT = 8080
s = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)

while True:
    testo = input("inserisci il messaggio: ")
    s.sendto(testo.encode(),(HOST,PORT))

    if(str(testo) == "stop"):
        break

    data,server = s.recvfrom(4096)
    print("ricevuto --> " + str(data) + "from --> " + str(server))

s.close()
print("socket chiuso")

