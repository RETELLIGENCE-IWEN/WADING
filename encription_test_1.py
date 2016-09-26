# module :: test_enc()

def maping(word):

    if (word == 'a'):
        x = 'xcv9'
        return(x)
    if (word == 'b'):
        x = 'xcc9'
        return(x)
    if (word == 'c'):
        x = 'xcv6'
        return(x)
    if (word == 'd'):
        x = 'dcv9'
        return(x)
    if (word == 'e'):
        x = 'xcv2'
        return(x)
    if (word == 'f'):
        x = 'xfv9'
        return(x)
    if (word == 'g'):
        x = 'xc45'
        return(x)
    if (word == 'h'):
        x = 'xqv9'
        return(x)
    if (word == 'i'):
        x = 'xct9'
        return(x)
    if (word == 'j'):
        x = 'tcv9'
        return(x)
    if (word == 'k'):
        x = 'xtt9'
        return(x)
    if (word == 'l'):
        x = 'xc11'
        return(x)
    if (word == 'm'):
        x = 'xcv0'
        return(x)
    if (word == 'o'):
        x = 'rrt9'
        return(x)
    if (word == 'n'):
        x = 'xrb9'
        return(x)
    if (word == 'p'):
        x = 'xyx9'
        return(x)
    if (word == 'q'):
        x = 'xvv9'
        return(x)
    if (word == 'r'):
        x = 'vcv9'
        return(x)
    if (word == 'x'):
        x = 'ocv9'
        return(x)
    if (word == 'y'):
        x = 'xqv5'
        return(x)
    if (word == 'z'):
        x = 'ggv9'
        return(x)
    if (word == 's'):
        x = 'pcv8'
        return(x)
    if (word == 't'):
        x = 'cc88'
        return(x)
    if (word == 'u'):
        x = 'qqv8'
        return(x)
    if (word == 'v'):
        x = 'xrv0'
        return(x)
    if (word == '1'):
        x = 'trt0'
        return(x)
    if (word == '2'):
        x = 'qwe0'
        return(x)
    if (word == '3'):
        x = 'asd6'
        return(x)
    if (word == '4'):
        x = 'zxc5'
        return(x)
    if (word == '5'):
        x = 'kjh8'
        return(x)
    if (word == '6'):
        x = 'xcc1'
        return(x)
    if (word == '7'):
        x = 'poi2'
        return(x)
    if (word == '8'):
        x = 'xyu4'
        return(x)
    if (word == '9'):
        x = 'xyt7'
        return(x)
    if (word == '0'):
        x = 'ghj8'
        return(x)


def change_with_key(ch, keyV):
    ch=ch.lower()
    asci=ord(ch)+int(keyV)
    if(ch.isdecimal()):
        if(asci>57):
           asci+=39
           if(asci>122):
               asci-=75
    else:
        if(asci>122):
            asci-=75
            if(asci>57):
                asci+=39
    val=chr(asci)
    return (val)
   



def test_enc(word, key):
    out = ''
    for el in word:
        el = change_with_key(el, key)
        out+=maping(el)

    return(out)



xxx = input("enter word  : ")
yyy = input("enter keyV  : ")
print(test_enc(xxx, yyy))


