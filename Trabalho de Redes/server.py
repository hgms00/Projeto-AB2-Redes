import socket, threading
import sys
from colors.Color import Color

class BinaryProtocol():
    def __init__(self,client_message):
        self.command = client_message.split('_')[0]
        self.message = client_message.split('_')[1]
        self.res = []
    
    def solve(self):
        if(self.command == 'CODIFICAR'):
            self.encode_solve()
        elif(self.command == 'DECODIFICAR'):
            self.decode_solve()
        else:
            return
        
        return self.res

       

    def encode_solve(self): 
        for letter in self.message:
            byte = ''.join(format(ord(letter), 'b'))

            if (len(byte) < 8):
                byte = '0' + byte
            self.res.append(byte)

    def decode_solve(self):
        binary_values = self.message.split()
        letter = ""

        for binary_value in binary_values:
            an_integer = int(binary_value,2)
            an_integer = chr(an_integer)
            letter += an_integer
            
        self.res.append(letter)



class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientAddress = clientAddress
        print (Color.GREEN + "New connection added: " , Color.BLUE, clientAddress)
    def run(self):
        print (Color.GREEN + "Connection from : " , Color.BLUE, clientAddress, Color.END)
        msg = ''
        while True:
            res = []
            data = self.csocket.recv(2048)
            msg = data.decode('utf-8')
            print ("From client ", Color.WARNING, self.clientAddress, ':' ,Color.BLUE, msg, Color.END)
            if msg=='DESCONECTAR':
                break

            protocol = BinaryProtocol(msg)
            res = protocol.solve()

            res_msg = ''
            for x in res:
                res_msg += x + ' '
            
            print ("To client",Color.WARNING, self.clientAddress, ':',Color.BLUE, res_msg, Color.END)
            self.csocket.send(bytes(res_msg,'UTF-8'))

        print ("Client at ",Color.BLUE,clientAddress , Color.RED + " disconnected..." + Color.END)


LOCALHOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))

print(Color.GREEN + "Server started" + Color.END)
print(Color.GREEN + "Waiting for client request.." + Color.END, '\n' * 2)

while True:
    try:
        server.listen(1)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()
    except: 
        break
server.close()