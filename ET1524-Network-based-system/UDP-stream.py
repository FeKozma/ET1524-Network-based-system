from socket import *
import time

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


host = '192.168.43.108'
port = 12000
serverPort = 12001

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', serverPort))


messageMaxLen = 100;
message = ''
for m in range(0, messageMaxLen):
	message += '0'

sequence = 10001

print("sending to " + host + ":" + str(port))
while True:
	s.sendto((str(sequence) + ';' + message).encode(), (host, port))
	sequence += 1

	time.sleep(1/nrPerSec)

