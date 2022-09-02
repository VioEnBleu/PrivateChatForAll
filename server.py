import socket
import select
import sys
from _thread import *
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Change this#
Port = 0
#############
 
server.bind(("", Port))

server.listen(100)

list_of_clients = []

print('===============\nServeur en ligne\n===============')

def clientthread(conn, addr):
 

    conn.send(f"[+] Tu a rejoinds la room".encode())
    
    m = f"[+] {addr[0]} a rejoinds la room".encode()
    
    print(m.decode())
    broadcast(m, conn)
    
    while True:
        try:
            message = conn.recv(2048)
            if message:   
                print (message.decode())
                message_to_send = message
                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except:
            continue
 
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message)
            except:
                clients.close()
                
                remove(clients)
 
def remove(connection):
    nbr=0
    if connection in list_of_clients:
        for i in list_of_clients:
            if i != connection:
                nbr += 1
            else:
                break
        list_of_clients.remove(connection)
 
while True:
    conn, addr = server.accept()
    
    list_of_clients.append(conn)    

    print (f"[+] Nouvelle connexion de {addr[0]}")
 
    start_new_thread(clientthread,(conn,addr))    
 
conn.close()
server.close()

