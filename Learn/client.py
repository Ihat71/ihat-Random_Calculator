import socket
import pickle #with this, you can create an object, pickle it then send it to the server then the server unpickles it and can use it. This way, you can send things that are not strings
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "Look, he disconected. "
SERVER = '192.168.1.4'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length)) #b'' is the byte representation of it
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
send('HELLO BRO')
input()
send(DISCONNECT_MESSAGE)