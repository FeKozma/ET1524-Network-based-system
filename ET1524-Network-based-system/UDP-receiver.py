from socket import *
import time
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 12000))

prevPacket = 10000

while True:
	message, serverAddress = s.recvfrom(2048)

	if prevPacket + 1 != int((message.decode())[:5]):
		print((message.decode())[:5])
	print((message.decode())[:5])
	prevPacket = int((message.decode())[:5])