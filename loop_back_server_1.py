# WAD test loop back server
import time
from socket import *

def get_ipaddress():
  s = socket(AF_INET, SOCK_DGRAM)
  s.connect(("gmail.com",80))
  r = s.getsockname()[0]
  print(s.getsockname())
  s.close()
  print('Server IP address : ', r)
  return (r)

serverIP = get_ipaddress()
server_port = 58446
addr = (serverIP, server_port)


serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverIP,server_port))
serverSocket.listen(1)
while (1):
  print("listening")
  connectionSocket, addr = serverSocket.accept()
  print("accepted")
  sentence = connectionSocket.recv(1024)
  print("recieved")
  if (sentence != None):
    print(sentence.decode())
    sentence = (sentence.decode() + 'Hello world')
    connectionSocket.send(sentence.encode())
  time.sleep(1)
  continue
