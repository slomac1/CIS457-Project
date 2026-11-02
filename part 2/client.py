from socket import *
import threading
from threadWorker import receive_messages

# Client socket setup
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('', 0))

clientRecievingThread = threading.Thread(target=receive_messages, args=(clientSocket,))
clientRecievingThread.start()

while True:
    # Get user input from client and send to server
    message = input('')
    if message.lower() == 'exit':
        break
    clientSocket.sendto(message.encode(), (serverName, serverPort))

clientSocket.close()
clientRecievingThread.join()