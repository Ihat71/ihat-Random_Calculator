import socket
import threading
import time
HEADER = 64 #gives us a set size of bytes the client can send to server
PORT = 5050 #above port 4000, the ports become inactive. 5050 is a safe port usually
#SERVER = '192.168.0.106' -use ipconfig in terminal to get your IPv4 address
#or
SERVER =  '192.168.1.4' #this auto gets your IPv4
ADDR = (SERVER, PORT) #ADDRESS needs to be a tuple of server and port
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'Look, he disconnected. ' #we need this to handle when a client disconnects
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#The first arg is the family, here it is 'over the internet'. It specifies the types of addresses we are looking for
#The second is the type
server.bind(ADDR)

def handle_client(conn, addr):
    #used to handle individual connections between 1 client and 1 server
    print(f'[NEW CONNECTION] {addr} connected.')
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #this is a blocking line of code, this allows you to tell you how many bytes you want to recieve from the client
        if msg_length:  
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            #sending = encode, recieving = decode
            print(f'{addr} {msg}') #this prints the address of the client and the message
            conn.send(f'msg recieved'.encode(FORMAT))
    conn.close() #closes the current connection
def start():
    #used to handle connections and distribute them to where they need to go
    server.listen() #listens for connections
    print(f'Listening to: {SERVER}')
    while True:
        conn, addr = server.accept() #server.accept() blocks and waits for a connection to the server and it creates an object which we can use to send info to the client
        #conn is the socket object, addr is the address of the connection (port and IP)
        thread = threading.Thread(target=handle_client, args = (conn, addr)) #we need threads since we have lines of codes which block so we need to circumvent that
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
    
print("Starting...")
start()