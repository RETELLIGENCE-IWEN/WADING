# communcationing with mobile app
# RETELLIGENCE IEZANOV IWEN

import threading
import time
from socket import *

mobile_list = []
port_list = []

def get_ipaddress():
  s = socket(AF_INET, SOCK_DGRAM)
  s.connect(("gmail.com",80)) 
  r = s.getsockname()[0]
  s.close()
  print('Server IP address : ', r)
  return (r)


def requesting(request):
# 받은 요청에 따라 클라언트에 정보 전송
    if request == '1':
      re = 'Heelo world'
    else:
      re = 'Hi'
    return(re)






def WADING_mobile(wading):
    global xx_code
    global x_code
    global serverIP
    global portMMM
    newport = wading[24:]

    Server_Tx_p = str(xx_code + wading[9:])
    serverSocket.send(Server_Tx_p.encode())
    
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((serverIP,newport))   
    serverSocket.listen(1)
    connectionSocket, addr = serverSocket.accept()
    
    while(inp != 0):
        time.sleep(3)
        sentence = connectionSocket.recv(1024)
        sentence = sentence.decode()
        
        if (sentence != None):
            while(len(sentence)!=0):
                if (sentence[:9] != x_code):      
                    break
                else:
                    wad = sentence[9:]
                    request = sentence[24:]
                    r = requesting(request)
                    re = xx_code + wad[9:24] + r
                    serverSocket.send(re.encode())
                    break 
        else:
            continue

        # out of loop

             

def communication_mobile():
    global serverIP = get_ipaddress()
    global portMMM = 14000
    global x_code = '###WAD*#*'  # Server Rx / WAD Tx
    global xx_code = '###WAD#*#' # Server Tx / WAD Rx
    global port_list
    
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((serverIP,portMMM))   
    serverSocket.listen(1)
    connectionSocket, addr = serverSocket.accept()

    while(1):
        time.sleep(3)
        sentence = connectionSocket.recv(1024)
        sentence = sentence.decode()
        
        if (sentence != None):
            while(len(sentence)!=0):
                if (sentence[:9] == x_code):
                    mobile_list.append(sentence[:24])
                    sentence = sentence[24:]
                else:
                    break

            for wading in mobile_list:
                private_port = 12000 + 1
                while(1):
                    if private_port in socket_list:
                        private_port += 1
                    else:
                        break
                port_list.append(private_port)
                # WAD info + port number
                wading = wading + str(private_port)

                th = WADING_moblie(wading)
                th.start()

            mobile_list = []
        else:
            continue
