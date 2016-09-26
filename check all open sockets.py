# check all open sockets

from socket import * 


import sys

the_yes_list=[]

def getadr():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("gmail.com",80))
    r = s.getsockname()[0]
    s.close()
    print('Server IP address : ', r)
    return (r)

targetIP = getadr()

##if ( len(sys.argv) != 2 ):
##    print ("Usage: " + sys.argv[0] + " you must enter IP or FQDN as argument")
##    sys.exit(1)
##    
##targetIP = gethostbyname(sys.argv[1])

for i in range(20, 65535):
    s = socket(AF_INET, SOCK_STREAM)
    result = s.connect_ex((targetIP, i))
    if(result == 0) :
        print (i, '11111111111111')
        the_yes_list.append(i)
    else:
        print(i, result)
    s.close()

print('\n \n \n \ndone')
