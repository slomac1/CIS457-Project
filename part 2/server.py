from socket import *
import threading
from threadWorker import receiveMessages

# Server socket setup
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

# Wait for initial message from client in order to get the clients address for sending messages
print("The server is waiting for client message to begin conversation")
initialMessage, clientAddress = serverSocket.recvfrom(2048)
print(initialMessage.decode())

# Thread worker for receiving messages from the client
serverRecievingThread = threading.Thread(target=receiveMessages, args=(serverSocket,))
serverRecievingThread.start()

while True:
    # Loop to continuously send messages to the client
    sendingMessage = input('')
    if sendingMessage.lower() == 'exit':
        break
    serverSocket.sendto(sendingMessage.encode(), clientAddress)

# Close the server socket and wait for the receiving thread to finish
serverSocket.close()
serverRecievingThread.join()