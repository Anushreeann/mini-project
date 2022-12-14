from base64 import encode
from pickle import TRUE
import socket



# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8001

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)
while TRUE:  
    
    # Wait for client connections
    client_connection, client_address = server_socket.accept()
    # Get the client request
    request = client_connection.recv(1024).decode()
    print("get request details:",request)
    filename =request.split()[1]
    f=open(filename[1:])
    outputdata = f.read()
    for i in range(0,len(outputdata)):
         client_connection.send(outputdata[i].encode())
    client_connection.sendall("\r\n".encode())

    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\n'
    client_connection.sendall(response.encode())
    client_connection.close()
     
server_socket.close()
