import socket
import select
import sys
from _thread import *
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
##########
Port = 
##########

server.bind(("", Port))

server.listen(100)

new = ""

list_of_clients = []

list_of_psedos = []

print('===============\nServeur en ligne\n===============')

def clientthread(conn, addr):
 

    conn.send(f"[+] Tu a rejoinds la room".encode())
    
    m = f"[+] {new} a rejoinds la room".encode()
    
    print(m.decode())
    broadcast(m, conn)
    
    while True:
        try:
            message = conn.recv(2048)
            if message:
                    if not '&' in message.decode():
                        print (message.decode())

                        message_to_send = message
                        broadcast(message_to_send, conn)
                    else:
                        m = message.decode()
                        n = m.rfind('>> ')
                        for i in range(0,n+3):
                            m=m[1:]
                        if m[0] == "&": 
                            m=m[1:]
                            if m == "list":
                                msg = ""
                                for i in list_of_psedos:
                                    msg+=f"[{i}] "
                                conn.send(f"[R0b0o-chan] Membres connectés : {msg}".encode())
                        
                        
                        else:
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
        list_of_psedos.remove(list_of_psedos[nbr])
        list_of_clients.remove(connection)
 
while True:

    
    conn, addr = server.accept()
    
    message = conn.recv(2048)
    
    try:
        new = message.decode()
    
        list_of_clients.append(conn)
        list_of_psedos.append(new)
    

        print (f"[+] Nouvelle connexion de {addr[0]}")
 
        start_new_thread(clientthread,(conn,addr))    
    except:
        continue
     
conn.close()
server.close()
