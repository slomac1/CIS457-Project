========================================================================
CIS 457 - Data Communications Project Part 1
========================================================================

GENERAL INFORMATION
-------------------
* Date 10/8/2026
* Group Members: Chase Sloma, Dominik Pathuis
* Github Repository Link: https://github.com/slomac1/CIS457-Project

PROJECT DESCRIPTION
-------------------
Two programs work together to form a UDP socket link between a local
client and server. Both the client and server will send a single message
before being shut down.

HOW TO RUN
----------
1. Dowload the zip file.
2. Extract the file into a folder location.
3. Open two terminal windows and navigate both to the previously selected
   folder.
4. In one window launch the server with command 'python server.py'.
5. Once server is running launch the client in the other window with
   command 'python client.py'.
6. Follow on screen instructions by first typing a message into the client.
7. Server will recieve and prompt for a reply message.
8. After both messages are sent and recieved, both client and server will 
   close their specific socket and exit. 
