from socket import *
import threading
from threadWorker import receive_messages

# Server socket setup
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is waiting for client message to begin conversation")
initial_message, clientAddress = serverSocket.recvfrom(2048)
print(initial_message.decode())

serverRecievingThread = threading.Thread(target=receive_messages, args=(serverSocket,))
serverRecievingThread.start()

while True:
    message = input('')
    if message.lower() == 'exit':
        break
    serverSocket.sendto(message.encode(), clientAddress)

serverSocket.close()
serverRecievingThread.join()