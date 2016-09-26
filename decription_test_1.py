# module :: test_dec()

def maping(word):

    if (word == 'xcv9'):
        x = 'a'
        return(x)
    if (word == 'xcc9'):
        x = 'b'
        return(x)
    if (word == 'xcv6'):
        x = 'c'
        return(x)
    if (word == 'dcv9'):
        x = 'd'
        return(x)
    if (word == 'xcv2'):
        x = 'e'
        return(x)
    if (word == 'xfv9'):
        x = 'f'
        return(x)
    if (word == 'xc45'):
        x = 'g'
        return(x)
    if (word == 'xqv9'):
        x = 'h'
        return(x)
    if (word == 'xct9'):
        x = 'i'
        return(x)
    if (word == 'tcv9'):
        x = 'j'
        return(x)
    if (word == 'xtt9'):
        x = 'k'
        return(x)
    if (word == 'xc11'):
        x = 'l'
        return(x)
    if (word == 'xcv0'):
        x = 'm'
        return(x)
    if (word == 'rrt9'):
        x = 'o'
        return(x)
    if (word == 'xrb9'):
        x = 'n'
        return(x)
    if (word == 'xyx9'):
        x = 'p'
        return(x)
    if (word == 'xvv9'):
        x = 'q'
        return(x)
    if (word == 'vcv9'):
        x = 'r'
        return(x)
    if (word == 'ocv9'):
        x = 'x'
        return(x)
    if (word == 'xqv5'):
        x = 'y'
        return(x)
    if (word == 'ggv9'):
        x = 'z'
        return(x)
    if (word == 'pcv8'):
        x = 's'
        return(x)
    if (word == 'cc88'):
        x = 't'
        return(x)
    if (word == 'qqv8'):
        x = 'u'
        return(x)
    if (word == 'xrv0'):
        x = 'v'
        return(x)
    if (word == 'trt0'):
        x = '1'
        return(x)
    if (word == 'qwe0'):
        x = '2'
        return(x)
    if (word == 'asd6'):
        x = '3'
        return(x)
    if (word == 'zxc5'):
        x = '4'
        return(x)
    if (word == 'kjh8'):
        x = '5'
        return(x)
    if (word == 'xcc1'):
        x = '6'
        return(x)
    if (word == 'poi2'):
        x = '7'
        return(x)
    if (word == 'xyu4'):
        x = '8'
        return(x)
    if (word == 'xyt7'):
        x = '9'
        return(x)
    if (word == 'ghj8'):
        x = '0'
        return(x)

# 수정이 필요한 함수 change with key
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
    x = 0
    while(len(word)!=0):
        word[x:x+4] = change_with_key(el, key)
        out+=maping(el)
        word = word[4:]

    return(out)



xxx = input("enter word  : ")
yyy = input("enter keyV  : ")
print(test_enc(xxx, yyy))


