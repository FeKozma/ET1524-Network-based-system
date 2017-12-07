# TCP Server
# Anders Nelsson BTH
# Exempel från kursbok

from socket import *

# get nr of udp utskick per sec
sentence = 'help';
while sentence == 'help':

    sentence = input('type help for help\ninput how many udp to send per second: ')
    if sentence == 'help':
        print('type in a nr\nex \'50\'\ne=empty\ntype \'low\' for 25 and \'high\' for 50')
    if (sentence == 'd') or (sentence == 'low'):
        sentence = "25"
    if sentence == 'high':
        sentence = '50'
    if sentence != 'help':
        try:
            nrPerSec = int(sentence)
        except:
            sentence = 'help'


serverPort = 12001


# create TCP welcoming socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))

# server starts listening for incoming TCP requests
serverSocket.listen(1)

print ('The TCP server is ready to receive')


messageMaxLen = 100;
message = ''
for m in range(0, messageMaxLen):
	message += '0'

sequence = 10001


# server waits for incoming requests; new socket created on return
connectionSocket, addr = serverSocket.accept()



while True:

    connectionSocket.send((str(sequence) + ';' + message).encode())
    sequence += 1
    time.sleep(1/nrPerSec)

    
# close the TCP connection; the welcoming socket continues
connectionSocket.close()

