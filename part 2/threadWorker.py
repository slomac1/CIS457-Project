def receive_messages(sock):
    while True:
        try:
            message = sock.recvfrom(2048)
            print(message[0].decode())
        except:
            print("Connection has been closed.")
            break