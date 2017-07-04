import socket
import time

HOST = "127.0.0.1"  # Endereco IP do Servidor
PORT = 5001           # Porta que o Cliente está

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
server = ('127.0.0.1', 5000)

print ("Digite S para sair")
udp.bind(dest)
msg = input("> ")
while True:
	ti = int(round(time.time()*1000))
	udp.sendto(msg.encode(), server)
	data, cliente = udp.recvfrom(1024)
	tf = int(round(time.time()*1000))
	if msg == "ping":
		print("Servidor",str(cliente),"responde: ",data.decode())
		print("Tempo: ",tf-ti,"ms")
		msg = input("> ")
	elif msg == "S":
		break
	else:
		msg = input("> ")
		
    
udp.close()
