import socket

serverName = '127.0.0.1'
serverPort = 12345

# Create a UDP socket at client side

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send to server using created UDP socket

sentence = input("Enter file name: ")
UDPClientSocket.sendto(bytes(sentence,"utf-8"),(serverName, serverPort))
filecontents,serverAddress = UDPClientSocket.recvfrom(2048)
print ('From Server:', filecontents)

UDPClientSocket.close()