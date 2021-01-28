import socket
from colors.Color import Color 
SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


class Command():
  def __init__(self,user_command):
    self.available_commands = ['CODIFICAR', 'DECODIFICAR', 'DESCONECTAR']
    self.command = ''
    for option in self.available_commands:
      if(option == user_command):
        self.command = user_command

  def textConcat(self,text):
    self.command += '_' + text

################################################
while True:

  while True:
    command_data = input('\n\nQue comando você pretende executar?\n\t -'+ Color.BLUE + ' CODIFICAR'+ Color.END +'\n\t -'+ Color.BLUE +' DECODIFICAR' + Color.END +'\n\t -'+ Color.BLUE + ' DESCONECTAR' + Color.END + '\n\n' + Color.PURPLE)
    print(Color.END)
    command_data = command_data.upper()
    
    class_command = Command(command_data)
    if(class_command.command != ''):
      break
    else:
      print('Digite um comando válido!')
      print('\nStatus Code: ', Color.RED, '400', Color.END)

  if command_data=='DESCONECTAR':
    client.sendall(bytes(class_command.command,'UTF-8'))
    break
  print('Status Code : ', Color.WARNING, '100\n', Color.END)  
  text_data = input('Digite o que você quer ' + Color.BLUE + class_command.command + Color.END + ':' + '\n\n' + Color.PURPLE)
  print(Color.END)
  class_command.textConcat(text_data)

  client.sendall(bytes(class_command.command,'UTF-8'))

  out_data = client.recv(1024)
  out_data = out_data.decode('utf-8')
  print("\n\nFrom server: " + Color.GREEN, out_data)
  print(Color.END, '\nStatus Code : ', Color.GREEN, '200', Color.END)
  print('\n' * 2)
client.close()