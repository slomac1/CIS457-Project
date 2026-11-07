from socket import *
import threading
from threadWorker import receiveMessages

# Client socket setup
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("Connected to server, ready to send messages. Type 'exit' to close the connection.")

# Thread worker for receiving messages from the server
clientRecievingThread = threading.Thread(target=receiveMessages, args=(clientSocket,))
clientRecievingThread.start()

while True:
    # Loop to continuously send messages to the server
    sendingMessage = input('')
    if sendingMessage.lower() == 'exit':
        break
    try:
        clientSocket.send(sendingMessage.encode())
    except:
        print("Error occurred while sending message.")
        break

# Close the client socket and wait for the receiving thread to finish
clientSocket.close()
clientRecievingThread.join()
print("Connection closed. Exiting client.")