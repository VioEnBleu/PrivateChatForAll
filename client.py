from socket import *
from threading import *
from tkinter import *

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

#########################
hostIp = ""
portNumber = 0
username = ""
#########################

clientSocket.connect((hostIp, portNumber))
clientSocket.send(username.encode("utf-8"))

window = Tk()
window.title("Untilted chat")

txtMessages = Text(window, width=50)
txtMessages.grid(row=0, column=0, padx=10, pady=10)

txtYourMessage = Entry(window, width=50)
txtYourMessage.grid(row=1, column=0, padx=10, pady=10)

def sendMessage():
    clientMessage = txtYourMessage.get()
    txtYourMessage.delete(0,"end")
    txtMessages.insert(END, "[Toi] >> "+ clientMessage + "\n")
    clientSocket.send(f"[{username}] >> {clientMessage}".encode("utf-8"))

btnSendMessage = Button(window, text="Send", width=20, command=sendMessage)
btnSendMessage.grid(row=2, column=0, padx=10, pady=10)

def recvMessage():
    while True:
        serverMessage = clientSocket.recv(2048).decode("utf-8")
        txtMessages.insert(END, serverMessage+"\n")

recvThread = Thread(target=recvMessage)
recvThread.daemon = True
recvThread.start()

window.mainloop()
