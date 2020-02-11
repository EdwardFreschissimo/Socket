import socket 
import random

def isPrime(n) : 
	# Corner cases 
	if (n <= 1) : 
		return False
	if (n <= 3) : 
		return True
	# This is checked so that we can skip 
	# middle five numbers in below loop 
	if (n % 2 == 0 or n % 3 == 0) : 
		return False
	i = 5
	while(i * i <= n) : 
		if (n % i == 0 or n % (i + 2) == 0) : 
			return False
		i = i + 6
	return True


s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#socket server 
s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket client
IPSERVERQUELLODOPO="192.168.10.110"
PORTA=8080
s1.bind(("0.0.0.0",8080))
s1.listen()
s2.connect((IPSERVERQUELLODOPO,PORTA))
conn1,clientAddress1=s1.accept()
print("Connesso con",conn1)
N=9973
g=1567
#N=input('inserisci N primo ')
#while isPrime(N)== False :
#   N=input('inserisci N primo ')
#g=random.randint(1,N)
print('g vale',g)
a=input('inserisci a')
while int(a)<1 or int(a)>N:
    a=input('inserisci a')

A= (g**int(a))%N
A=b'A'

    s2.sendall(A)
    B=conn1.recv(4096).decode()
    print("client :",(clientAddress1,B))
    if(B=="EXIT"):
        break
    
conn1.close()
s1.close()
s2.close()
k=(B**a)%N
print('Il numero è',k)