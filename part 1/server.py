from socket import *

# Server socket setup
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

# Decoding and displaying message received from client
message, clientAddress = serverSocket.recvfrom(2048)
print(f"Message received: {message.decode()}")

# Getting user input from server and sending to client
message = input('Input reply message: ')
serverSocket.sendto(message.encode(), clientAddress)

# Process complete and closing socket
print("Message sent to client, shutting down")
serverSocket.close()