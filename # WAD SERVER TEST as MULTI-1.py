# WAD SERVER (DRONE JONGHAP GUWANJE SYSTEM)

# Licence      Isaac Kim-leader of team RETELLIGENCE
# 2016


import threading
from socket import *
import time
import os
import random
from datetime import datetime


print('**************************************************************************')
print('*     start_THE_First_WADING_Connection_VIA_RETELLIGENCE_IEZANOV_IWEN    *')
print('**************************************************************************')

# make file directory 
#os.makedirs('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen')

# open file
# file handle

#F_users_h = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\User_info.txt', '+')

# file read
#R_users_h = F_users_h.read()

F_users_h = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\WAD_pinList.txt', '+') # loading pin data from DBMS
WAD_pinList = []
R_users_h = F_users_h.read()
C_users_h = R_users_h  # copy of pin data

while(1): # loading pin data for making user ID 
    try:        
        for i in range(len(C_users_h)):
            if (C_users_h[i]=='#') and (C_users_h[i+1]=='#') and (C_users_h[i+2]=='#'):
                WAD_pinList.append((C_users_h[i+3:i+12])
    except:
        break



# preset list
# 12000~24000 WAD
# 24000~36000 app
# 36000~48000 platform

Server_Rx_prot_len = 24
Server_TX_prot_len = 


server_adr = getadr()

LIVE_WAD_list = []


x_code = '###WAD*#*'  # Server Rx / WAD Tx
xx_code = '###WAD#*#' # Server Tx / WAD Rx
re_list = []


## WAD ##

    # step 1
    """
    Server_Rx_prot =
        1.[9]  ###WAD*#*
        2.[9]  ID : _ _ _  _ _ _ _  _ _
        3.[6]  PW : _ _ _ _ _ _
        """


    # step 2n
    """
    Server_Tx_prot =
        1.[9]  ###WAD#*#
        2.[5]  New Port number
        3.[6]  PW : _ _ _ _ _ _
        4.[5]  command : _ _ _ _ _
        """


    # step 2n+1
    """
    Server_Rx_data =
        1.[9]   x_code (###WAD*#*)
        2.[9]   ID
        3.[6]   PW
        4.[6]   status
        5.[128]  beacon
        """


## APP ##




## PLATFORM ##

    # step 1
    """
    Server_Rx_prot =
        1.[9] x_code
        2.[9] ID
        3.[6] PW
        """

    # step 2
    """

    """





def check_multi_id(id_give): # check if some one is using same id (register sequence on app)
    if id_give in R_users_h:
        return (1)
    else:
        return(0)


def getadr():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("gmail.com",80))
    r = s.getsockname()[0]
    s.close()
    print('Server IP address : ', r)
    return (r)


def check_prot(wad_info):
    pass


def disconnect_all():
    serverSocket.close()
    sys.exit()
    print("Manually disconnected..")
    time.sleep(0.5)
    for i in range(9)
        print("Programm will automaticly quit in %s seconds.." % str(9-int(i)))
        time.sleep(1)
    quit()
    

def save_leftover():
    pass


def start_socket():

    server_adr = getadr()

    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((server_adr, main_port))
    serverSocket.listen(1)
    connectionSocket, addr = serverSocket.accept()

##
### RETELLIGENCE WADING IN--on new thread  
##class WADING(threading.Tread):
##
##    def run(self, WAD):
##
##        #  WAD[0:9]   = x_code
##        #  WAD[9:18]  = WAD id
##        #  WAD[18:24] = WAD pw
##        #  WAD[24:29] = WAD new Port number
##
##        given_PW = 
##        State = 'protocal_initializing'
##
##        ### SERVER TX PROTOCALL DATA PACKET
##        serverTx_protocall = xx_code + str(private_port) + '/' + str(given_PW) + '/' + str(State) + '/'
##
##        ### socket BIND      
##        serverSocket = socket(AF_INET,SOCK_STREAM)
##        serverSocket.bind((server_adr, private_port))
##        serverSocket.listen(1)
##        connectionSocket, addr = serverSocket.accept()
##        connectionSocket.send = (serverTx_protocall.encode())
##
##        recv_data = erverSovket.recv(1024)
##
##        if (recv_data[0:9] == x_code):
##            print(recv_data[9:18], '  recieving')            
##            a
##        # error => break
##        # what is suspend
##        
##
##
##
##start_socket()
##
##
##while(1):
##    request_list = []
##    input_WAD = connectionSocket.recv(2048)
##    while(1):
##        if input_WAD != None:
##
##            # length check
##            if len(input_WAD)%24 == 0:
##                
##                # encription check
##                if input_WAD[0:9] == x_code:
##                    ident_info = input_WAD[9:24]
##                    ident_info = '[' + ident_info + ']'
##                    if ident_info in WAD_ident_list:
##                    # send to request list
##                    request_list.append(input_WAD[0:24])
##
##                    # iteration go
##                    input_WAD = Input_WAD[24:]
##                    continue
##        else:
##            break
##
##
##
##
##    for WAD in reauest_list:
##
##        print('Starting new chapter')        
##        # set private port
##        private_port = 12000 + 1
##        while(1):
##            if private_port in socket_list:
##                private_port += 1
##            else:
##                break
##        socket_list.append(private_port)
##
##        # WAD send new port number
##        Server_Tx_p = str(xx_code + private_port)
##        serverSocket.send(Server_Tx_p.encode())
##
##        # WAD info + port number
##        WAD = WAD + str(private_port)
##
##
##        # thread starting
##        print(WAD)
##        th = WADNIG(WAD)
##        th.start()
##
##    ## NOW U MAY ENTER WAD PROTOCAL
    ## WELCOME TO THE WORLD WIDE ASOCCIATION OF DRONES VIA INTERCONNECTED NETWORK INTEGERATION - RETELLIGENCE IWEN IEZANOV


    


#if 'Name' == __Main__:




def WADING(port):

    while(1):
        server_adr = getadr()
        serverSocket = socket(AF_INET,SOCK_STREAM)
        serverSocket.bind((server_adr, port))
        serverSocket.listen(1)
        connectionSocket, addr = serverSocket.accept()

        while(1):
            in_1 = connectionSocket.recv(1024) # recieve from wad
            if in_1[:9] != x_code:
                printQ("!!! Unidentified connection", port, str(datetime.now())
                connectionSocket.close()
                break
                
            id_1 = in_1[9:15]
            printQ("$$ Port", port, 'connected for WAD :: ', id_1, str(datetime.now())






            connectionSocket.send(server_Rx_wad)






def APP(port):
                   
    def Make_id_i(): 
        global WAD_pinlist

        type_WAD = 'i'
        year_WAD = str((time.localtime(time.time()))[0])
        pin_WAD = str(int(WAD_pinList[-1]) + 1)
        if len(pin_WAD) > 4:
            pin_WAD = pin_WAD[0:4]

        ID_WAD = type_WAD + year_WAD[-2] + year_WAD[-1] + '0'*(4-len(pin_WAD)) + str(random.randint(11,99))

        while(1):
            if check_multi_id(ID_WAD) = 1:
                ID_WAD = ID_WAD[0, 7] + str(random.randint(11,99))
                continue
            else:
        while(1):
            passward = input("Enter PW (6 numbers): ")
            try:
                passward = int(passward)
            except:
                continue
            else:
                if len(passward) != 6:
                    continue
                elif len(passward) == 6:
                    break
                break
        print(ID_WAD)
        print(passward)
        stat = ('Confirm?(y/n) : ')
        if stat == 'y':
            write_info = '[' + ID_WAD + +', ' + str(passward) + ']'

            WAD_pinList.append(pin_WAD)




    server_adr = getadr()
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((server_adr, port))
    serverSocket.listen(1)
    connectionSocket, addr = serverSocket.accept()

    in_1 = connectionSocket.recv(1024) # recieve from app
    id_1 = in_1[9:15]
    printQ("$$ Port", port, 'connected for app :: ', id_1, str(datetime.now())






def PLATFORM(port):
                   
    def Make_id_s(): 
        global WAD_pinlist

        type_WAD = 's'
        year_WAD = str((time.localtime(time.time()))[0])
        pin_WAD = str(int(WAD_pinList[-1]) + 1)
        if len(pin_WAD) > 4:
            pin_WAD = pin_WAD[0:4]

        ID_WAD = type_WAD + year_WAD[-2] + year_WAD[-1] + '0'*(4-len(pin_WAD)) + str(random.randint(11,99))

        while(1):
            if check_multi_id(ID_WAD) = 1:
                ID_WAD = ID_WAD[0, 7] + str(random.randint(11,99))
                continue
            else:
        while(1):
            passward = input("Enter PW (6 numbers): ")
            try:
                passward = int(passward)
            except:
                continue
            else:
                if len(passward) != 6:
                    continue
                elif len(passward) == 6:
                    break
                break
        print(ID_WAD)
        print(passward)
        stat = ('Confirm?(y/n) : ')
        if stat == 'y':
            write_info = '[' + ID_WAD + +', ' + str(passward) + ']'

            F_users_h.write('\n')
            F_users_h.write(write_info)
            F_users_h.write('\n')
            WAD_pinList.append(pin_WAD)



    server_adr = getadr()
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((server_adr, port))
    serverSocket.listen(1)
    connectionSocket, addr = serverSocket.accept()
    
    in_1 = connectionSocket.recv(1024) # recieve from platform
    id_1 = in_1[9:15]
    printQ("$$ Port", port, 'connected for platform :: ', id_1, str(datetime.now())










def printQ(sent):
    global prints
    if prints == True:
        print(sent)

def initial_WAD():
    for i in range(12000, 24000):
        WADING(i)


def initial_APP():
    for j in range(12000, 24000):
        APP(j)


def initial_PLATFORM():
    for k in range(12000, 24000):
        PLATFORM(k)


        
def initialize(): # called by main()
    
    # thread for each type of connection setting
    init_wad = threading.Thread(target=initial_WAD)
    init_app = threading.Thread(target=initial_APP)
    init_platform = threading.Thread(target=initial_PLATFORM)

    # starting tread for initializing step 1
    init_wad.start()
    init_app.start()
    init_platform.start()
    



def main(): # main function
    global prints

    initialize() # calling initializing mode


    while(1):
        # start managing server
        
        stat = input('[ Server Setup : s ]  [ Variable Setings : v ]  [ Admin Menu : a ]  [ Live view : i ]  [ Emergency Proxy Shut-down : e ] ')


        if (stat == 's')or(stat == 'a')or(stat == 'v'):
            print('$ Comming soon...')

        if stat == 'i':
            while(1):
                print_ask = input("$ Press 'enter' to go on")
                if print_ask='':
                    prints = True  # global var to alow system to print to consol about system flow
                else:
                    prints = False
                    break
                time.sleep(10)
                    
        if stat == 'e':
            disconnect_all()
            


if (__name__ == "__main__"): # modulize
    main()

        
