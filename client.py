from socket import *

# Client socket setup
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Get user input from client and send to server
message = input('Input message to send: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))

print("Waiting for reply from server...")

# Recieved message from server and displaying
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

# Process complete and closing socket
print("Reply received, shutting down")
clientSocket.close()