from socket import *
import threading
from threadWorker import receiveMessages

# Server socket setup
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

# Wait for client connection in order to get the clients address for sending messages
print("The server is waiting for client connection to begin conversation")
clientSocket, clientAddress = serverSocket.accept()
print(f"Connection established with {clientAddress}. Ready to receive and send messages, type 'exit' to close the connection.")

# Thread worker for receiving messages from the client
serverRecievingThread = threading.Thread(target=receiveMessages, args=(clientSocket,))
serverRecievingThread.start()

while True:
    # Loop to continuously send messages to the client
    sendingMessage = input('')
    if sendingMessage.lower() == 'exit':
        break
    try:
        clientSocket.sendto(sendingMessage.encode(), clientAddress)
    except:
        print("Error occurred while sending message.")
        break

# Close the sockets and wait for the receiving thread to finish
serverSocket.close()
clientSocket.close()
serverRecievingThread.join()
print("Connection closed. Exiting server.")