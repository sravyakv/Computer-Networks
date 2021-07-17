import socket

serverName = '127.0.0.1'
serverPort = 12345

# Create a datagram socket

UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((serverName, serverPort))

print("UDP server up and listening")

# Listen for incoming datagrams

while (True):
    sentence, clientAddress = UDPServerSocket.recvfrom(2048)

    file = open(sentence, "r")
    l = file.read(2048)

    UDPServerSocket.sendto(bytes(l, "utf-8"), clientAddress)
    print("sent back to client: ", l)
file.close()