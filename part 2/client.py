from socket import *
import threading
from threadWorker import receiveMessages

# Client socket setup
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('', 0))

# Thread worker for receiving messages from the server
clientRecievingThread = threading.Thread(target=receiveMessages, args=(clientSocket,))
clientRecievingThread.start()

while True:
    # Loop to continuously send messages to the server
    sendingMessage = input('')
    if sendingMessage.lower() == 'exit':
        break
    clientSocket.sendto(sendingMessage.encode(), (serverName, serverPort))

# Close the client socket and wait for the receiving thread to finish
clientSocket.close()
clientRecievingThread.join()