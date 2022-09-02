import socket
import select
import sys
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

###Things you NEED to change###
Port = 0
IP = ""
username = ""
###############################

server.connect((str(IP), Port))

while True:
 
    sockets_list = [sys.stdin, server]

    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            if message:
                print (message.decode())
        else:
            
            message = sys.stdin.readline()
            
            server.send(f"[{username}] >> {message}".encode())
            sys.stdout.write("[Toi] >> ")
            sys.stdout.write(message)

server.close()
