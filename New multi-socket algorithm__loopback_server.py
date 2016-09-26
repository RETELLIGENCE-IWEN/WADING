# New tread-socket algorithm test

import threading
from socket import *
import time
import datetime

addrS = []
port_list = []
x_code = "###WAD*#*"
xx_code = "###WAD#*#"

def TN():
    time1 = datetime.datetime.now().time()
    time1 = time1.isoformat()
    time1 = time1[:8]
    print(time1)
    return(time1)

def get_ipaddress():
  s = socket(AF_INET, SOCK_DGRAM)
  s.connect(("gmail.com",80)) 
  r = s.getsockname()[0]
  s.close()
  print('Server IP address : ', r)
  return (r)

serverIP = get_ipaddress()
serverPort = 12000
threads = []
print("\ninitialized\n")

for i in range(10):
    app = (serverIP, serverPort)
    addrS.append(app)
    port_list.append(serverPort)
    serverPort += 1

print("\naddr set\n")

class comm(threading.Thread):

    def __init__(self, addr):
        self.addr = addr

    def run(self):
        print(addr, "starting")
        serverSocket = socket(AF_INET,SOCK_STREAM)
        serverSocket.bind((addr))
        serverSocket.listen(1)
        connectionSocket, addr = serverSocket.accept()
        print(addr, "accepted")
        while(1):
            time.sleep(3)
            sr = connectionSocket.recv(1024)
            sr = sr.decode()
            if sr == None:
                print("no input")
            else:
                print(TN(), '    : ', sr)
                time.sleep(0.5)
                reaction = "Hello WAD"
                connectionSocket,send(reaction)
            continue

def Main():
    global addr
    for addr in addrS:
        print(addr)
        t1 = threading.Thread(target=comm, args=(addr))
        threads.append(t1)
        t1.start()
      
##    for i in threads:
##        i.join()
##    print("all threads initialized")

Main()
    



##
##if "__name__" == __Main__:
##    Main()
