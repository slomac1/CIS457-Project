def receiveMessages(sock):
    while True:
        # Continuously listen for incoming messages from the socket
        try:
            receivingMessage = sock.recvfrom(2048)
            print(receivingMessage[0].decode())
        # Listener closes if an error occurs
        except:
            print("Connection has been closed.")
            break