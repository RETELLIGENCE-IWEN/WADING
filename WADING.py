###############################################################################################
## WAD SERVER (DRONE JONGHAP GUWANJE SYSTEM)                                                                                                    
##                                                                                                                                                                                        
## Isaac Kim   leader of team RETELLIGENCE                                                                                                                      
##                                                                                                                                                                                        
##    MIT License                                                                                                                                                               
##                                                                                                                                                                                        
##    Copyright (c) [2016] [Isaac Kim]                                                                                                                                 
##                                                                                                                                                                                        
##    Permission is hereby granted, free of charge, to any person obtaining a copy            
##    of this software and associated documentation files (the "Software"), to deal           
##    in the Software without restriction, including without limitation the rights            
##    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell           
##    copies of the Software, and to permit persons to whom the Software is                   
##    furnished to do so, subject to the following conditions:                                
##                                                                                            
##    The above copyright notice and this permission notice shall be included in all          
##    copies or substantial portions of the Software.                                         
##                                                                                            
##    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR              
##    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,                
##    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE             
##    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER                  
##    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,           
##    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN           
##    THE SOFTWARE.                                                                               
##                                                                                            
##    RETELLIGENCE                                                                        
##                                                                                            
###############################################################################################


###############################################################################################
##                                                                                            
## Recommended operating system                                                               
## OS : over windows 10 home                                                                  
## cpu : over 8 hardware threads, over 3.2Ghz clock speed
## RAM : over 32GB of memory capacity, same or higher speed of DDR4
## Internet connention : over 1GB/s                                                           
## Required software : python 3.5.2                                                           
##                                                                                            
## Socket port 12100, 12200, 12300, 14000 must be unused                                                           
##                                                                                            
###############################################################################################


###############################################################################################
##                                                                                                                                  
## Project Definition Keywords                                                                
##                                                                                            
## WADING : World-wide Assocciation of Drones via Interconnected Network Integration          
## WAD : chip that enables WADING, will be attached to Drones                                 
## APP : mobile app for drone owners. used for WADING operation                               
## PPG(Platform Programm) : programm for atonomos drone owners like amazone                   
##                                                                                            
###############################################################################################


# Library importing
from socket import *
import threading
import time
from datetime import datetime
from urllib.request import urlopen
import os


master_K = 'retelligence'

# get operating system's ipv4 address : used as server IP address
def getadr(): 
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("gmail.com",80))
    r = s.getsockname()[0]
    s.close()
    return (str(r))


# Change GPS coordinate to Cubic coordinate
def CUBIC_gps_to_cubic(lat, lon, height):
    
    # lat_dms 30m = 1sec
    # lon_dms 30m = 1.25sec
    # lat_dd 30m = 0.000277
    # lom_dd 30m = 0.000347

    lt_1 = 0.000277
    lo_1 = 0.000347

    Ground_Zero = [37.60000, 126.86466, 0]
    Ground_Zero_as_CUBIC = [0, 0, 0]

    x = int(0 - ((Ground_Zero[0]-float(lat))//lt_1))
    y = int(0 - ((Ground_Zero[1]-float(lon))//lo_1))
    z = int(0 - ((Ground_Zero[2]-float(height))//30))-1

    CUBIC_cd = '[' + '0'*(6-len(str(x))) + str(x) + ', ' +'0'*(6-len(str(y))) + str(y) + ', ' + '0'*(6-len(str(z))) + str(z) + ']'
    return(CUBIC_cd)

    # return example : [0-2166, 003272, 000000] // as string


# Change Cubic coordinate to GPS coordinate
def CUBIC_cubic_to_gps(x, y, z):

    # lat_dms 30m = 1sec
    # lon_dms 30m = 1.25sec
    # lat_dd 30m = 0.000277
    # lom_dd 30m = 0.000347

    lt_1 = 0.000277
    lo_1 = 0.000347

    Ground_Zero = [37.60000, 126.86466, 0]
    Ground_Zero_as_CUBIC = [0, 0, 0]

    x_c = Ground_Zero [0]+ ((0 - (Ground_Zero_as_CUBIC[0]-x))*lt_1)
    y_c = Ground_Zero [1]+ ((0 - (Ground_Zero_as_CUBIC[1]-y))*lo_1)
    z_c = Ground_Zero [2]+ ((0 - (Ground_Zero_as_CUBIC[2]-z))*30)+15

    x_cd = round(x_c, 6)
    y_cd = round(y_c, 6)
    z_cd = round(z_c, 6)

    GPS_cd = '[' + str(x_cd) + ', ' + str(y_cd) + ', ' + str(z_cd) + ']'
    return(GPS_cd)

    # return example : [37.600000, 1286.86466, 15] // as string


        
def CUBIC_chk(x, y, z):
    xx = 0
    yy = 0
    # got input of (lat, lon, alt)
    cub = CUBIC_gps_to_cubic(x, y, z)
    cab = len(cub)
    print('CUBIC location   : ', cub)

# parsing X coordinate
    for i in range(cab):
        if (cub[i]==','):
            xx = i
            break
    x_cd = cub[1:xx]
    for i in range(len(x_cd)):
        if x_cd[i]=='-':
            x_cd = x_cd[i+1:]
            break

# parsing Y coordinate
    for i in range(xx+2, cab):
        if cub[i]==',':
            yy = i
            break
    y_cd = cub[xx+2:yy]
    for i in range(len(y_cd)):
        if y_cd[i]=='-':
            y_cd = y_cd[i+1:]
            break

# parsing Z coordinate
    z_cd = cub[yy+2:-1]
    
    x_cd, y_cd, z_cd = int(x_cd), int(y_cd), int(z_cd)
##    print('X : ', x_cd)
##    print('Y : ', y_cd)
##    print('Z : ', z_cd)

    if z_cd>5:
        return('Altitude Out of Range')

    if (x_cd>=0) and (y_cd>=0):
        fh = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\CUBIC_sys_m1.txt', 'r')
        rh = fh.read()
##        print('opening CUBIC_sys_m1')

    if (x_cd>0) and (y_cd<0):
         fh = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\CUBIC_sys_m2.txt', 'r')
         rh = fh.read()
##         print('opening CUBIC_sys_m2')

    if (x_cd<0) and (y_cd>0):
         fh = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\CUBIC_sys_m3.txt', 'r')
         rh = fh.read()
##         print('opening CUBIC_sys_m3')

    if (x_cd<0) and (y_cd<0):
         fh = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\CUBIC_sys_m4.txt', 'r')
         rh = fh.read()
##         print('opening CUBIC_sys_m4')


    ind = 0
    while(1):
        try:
            if rh[ind:ind+22] == cub:
                fh.close()
                return('In Usaage')
            else:
                fh.close()
                return('Avaliable')
        except:
            fh.close()
            return('Avaliable')
        else:
            ind += 1


    


 # Handeling Client connection WAD
def clientHD_wad(conn, addr):
    while(1):
        try:
            xx=0
            yy=0
            Rx = (conn.recv(1024)).decode()
            if '###WAD*#*' not in Rx:
                break
            lock.acquire()
            print("\n$ WAD port : ", addr, "  >>  ", '@', str(datetime.now()))
            
            for i in range(len(Rx)):
                if Rx[i]=='/':
                    xx=i+1
                    break
            x_cd = Rx[9:xx-1]

            for i in range(xx, len(Rx)):
                if Rx[i]=='/':
                    yy=i
                    break
            y_cd = Rx[xx:yy]

            for i in range(yy+1, len(Rx)):
                if Rx[i]=='/':
                    xx = i
                    break
            z_cd = Rx[yy+1:xx]

            for i in range(xx+1, len(Rx)):
                if Rx[i] == '/':
                    yy = i
                    break
            speed = Rx[xx+1:yy]

            WAD_id = Rx[yy+1:]

            print('--WAD ID--   : ' , WAD_id)
            print('Longitude : ', x_cd)
            print('Latitude    : ', y_cd)
            print('Altitude     : ', z_cd, 'm')
            print('Speed      : ', speed, 'Km/h')
            print('Flight avaliability : ', CUBIC_chk(str(x_cd), str(y_cd), str(z_cd)))
            lock.release()
            
        except:
            lock.acquire()
            print("\n$ >> Client error  >>  ", addr, '@', str(datetime.now()))
            lock.release()
            conn.close()
            break


 # Handeling Client connection APP
def clientHD_app(conn, addr):

## communication code with app and server
    log_CODE = 'qwe123' # can I login? yes you can login
    register_CODE = 'asd123' # can I registor? yes you may
    fl_ass_CODE = 'zxc123' # I want to see geological data arround me! sure : flight assistance
    trace_CODE = 'rty123' # I want to trace my drone! here you go
    flight_reg_CODE = 'fgh123' # I want to register cubics! go ahead
    donate_CODE = 'vbn123' # I want to donate! thanks

    # login fail : ewq321
    # real time tracking fail (invalid id or pw) : ytr123
    # real time tracking fail (WAD offline) : ytr321
    # cubic sys fail (WAD offline) : hgf321
    # cubic sys fail (already in use) : hgf123
    # fail to registor (use different id) : dsa123 


    
    while(1):
        try:
            Rx = conn.recv(1024)
            Rx = Rx.decode()
            if '###WAD*#*' not in Rx:
                break
            lock.acquire()
            print("\n$ APP port : ", addr, "  >>  ", '@', str(datetime.now()))
            print(Rx)
            lock.release()
        except:
            lock.acquire()
            print("\n$ >> Client error  >>  ", addr, '@', str(datetime.now()))
            lock.release()
            conn.close()
            return(0)
        else:
            print(1)
            break
    

    print(2)
    request = Rx[9:15]
    print('Request Code : ', request)


## login start
    if request == log_CODE:

        for i in range(len(Rx)):
            try:
                if Rx[i:i+4]=='123#':
                    id_s = i+4
                    break
            except:
                lock.acquire()
                print("\n$ >> Non-WAD Client   >>  ", addr, '@', str(datetime.now()))
                lock.release()
                return(0)

        for i in range(id_s, len(Rx)):
            if Rx[i]=='/':
                id_e = i
                break
        
        user_id = Rx[id_s:id_e]
        ui_len = len(user_id)
        user_pw = Rx[id_e+1:]
        up_len = len(user_pw)
        
        login_access = 0
        lock.acquire()
        fh = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\User_registor.txt', 'r')
        rh = fh.read()
        fh.close()
        lock.release()
       
        print('request id : ', user_id)
        print('request pw : ', user_pw)

        for i in range(len(rh)):    
            try:
                if rh[i:i+ui_len]==user_id:
                    if rh[i+ui_len+2:i+ui_len+2+up_len]==user_pw:
                        
                        try:
                            login_access = 1
                            lock.acquire()
                            print("\n$ >> Client Login success  >>  ", addr, user_id,  '@', str(datetime.now()))
                            lock.release()
                            conn.send(('###WAD#*#qwe123').encode()) # login success
                        except:
                            lock.acquire()
                            print("\n$ >> Client error  >>  ", addr, '@', str(datetime.now()))
                            lock.release()
                            conn.close()
                            return(0)
                        else:
                            lock.acquire()
                            live_APP.append(user_id)
                            lock.release()
                            conn.close()
                            return(0)
            except:
                break
            
        if login_access != 1: # login fail
            lock.acquire()
            print("\n$ >> Client Login Failed  >>  ", addr, '@', str(datetime.now()))
            lock.release()
            try:
                conn.send(('###WAD#*#ewq321').decode())
            except:
                lock.acquire()
                print("\n$ >> Client error  >>  ", addr, '@', str(datetime.now()))
                lock.release()
            finally:
                conn.close()
                return(0)

        else: # loged in
            conn.close()
            return(0)
## login end
                                        

                            





    elif request == register_CODE:
       pass



  
## real-time monitering start
    elif request == trace_CODE:

        for i in range(len(Rx)):
            try:
                if Rx[i:i+4]=='123#':
                    id_s = i+4
                    break
            except:
                lock.acquire()
                print("\n$ >> Non-WAD Client   >>  ", addr, '@', str(datetime.now()))
                lock.release()
                break

        for i in range(id_s, len(Rx)):
            if Rx[i]=='/':
                id_e = i
                break

        user_id = Rx[id_s:id_e]

        lock.acquire()
        fh = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\User_registor.txt', 'r')
        rh = fh.read()
        fh.close()
        lock.release()
        

        if wad_id not in live_WAD:
            lock.acquire()
            print("\n$ >> Real-Time monitering :: WAD not online  >>  ", addr, user_id, ' >> ', wad_id, str(datetime.now()) )
            lock.release()
            try:
                conn.send(('###WAD#*#ytr321'))
            except:
                lock.acquire()
                print("\n$ >> Client error  >>  ", addr, '@', str(datetime.now()))
                lock.release()
            finally:
                conn.close()

        else: ## WAD online!
            while(1):
                pass
            


        
     
      
## real-time monitering end




    elif request == flight_reg_CODE:
        pass


    else:
        print('\n$ APP port : ',  addr, '  >>  unidentified request', '@', str(datetime.now()))
        



def WAD_controll():    
    addrs = (getadr(), 12100)
    server = socket(AF_INET, SOCK_STREAM)
    ##server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addrs)
    server.listen(100)
    # denotes the number of clients can queue (10)
    
    while(1):
        try:
            conn, addr = server.accept()
            t1 = threading.Thread(target = clientHD_wad, args=(conn, addr, ))
            lock.acquire()
            print("\n$ >> New connection  >>  ", addr, '@', str(datetime.now()))
            lock.release()
            t1.start()
        except:
            lock.acquire()
            print("\n$ Server error : failed to accept clients : WAD controll", addr, '@', str(datetime.now()))
            lock.release()
##            conn.shutdown(1)
##            server.shutdown(1)
            conn.close()
            server.close()
            quit()
        else:
            continue



def APP_controll():    
    addrs = (getadr(), 12200)
    server = socket(AF_INET, SOCK_STREAM)
    ##server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addrs)
    server.listen(10)
    # denotes the number of clients can queue (10)

    while(1):
        try:
            conn, addr = server.accept()
            t1 = threading.Thread(target = clientHD_app, args=(conn, addr, ))
            lock.acquire()
            print("\n$ >> New connection  >>  ", addr, '@', str(datetime.now()))
            lock.release()
            t1.start()
        except:
            lock.acquire()
            print("\n$ Server error : failed to accept clients : APP controll", addr, '@', str(datetime.now()))
            lock.release()
##            conn.shutdown(1)
##            server.shutdown(1)
            conn.close()
            server.close()
            quit()
        else:
            continue



def MAIN():
    # Server login
    while(1):
        global master_K
        init_stat = input("Enter PW : ")
        if (init_stat == master_K): # correct passward
            break

        if (init_stat == master_K + '#'): # correct passward + #
            while(1):
                master_K = input("New PW : ")
                stat = input("Confirm? : ")
                if (stat==''):
                    print("Log in again")
                    break
                else:
                    continue


    # ask initialize
    while(1):
        stat = input("Initialize? : ")
        if stat == '':
            break
        else:
            continue

        
    # Server initialize

        
    print('Server IP : ', getadr())
    server_start_time = datetime.now()
    print('**************************************************************************')
    print('*         Start THE First WADING Connection via RETELLIGENCE IEZANOV IWEN         ')
    print('*                                                                                                                              ')
    print('*                                      ', str(server_start_time), '                                               ')
    print('**************************************************************************')
    print('\n \n \n \n')

    global lock
    lock = threading.Lock()

    global live_WAD
    live_WAD = []

    global live_APP
    live_APP = []

    try:
        wadC = threading.Thread(target=WAD_controll)
        appC = threading.Thread(target=APP_controll)
        wadC.start()
        appC.start()
    except:
        print("\n$ System Initialize Error : failed to start operations", '@', str(datetime.now()))
    else:
        print("\n$ System Initialize complete", '@', str(datetime.now()))
        print("----------------------------------------------------")

    



MAIN()






