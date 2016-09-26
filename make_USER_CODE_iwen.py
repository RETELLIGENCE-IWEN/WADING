import datetime
import random


def ran():
    code = ''
    for i in range(3):
        x = random.randint(0, 24)
        if x == 0:
            code += 'h'
        if x == 1:
            code += 'b'
        if x == 2:
            code += 'c'
        if x == 3:
            code += 'd'
        if x == 4:
            code += 'e'
        if x == 5:
            code += 'f'
        if x == 6:
            code += 'g'
        if x == 7:
            code += 'a'
        if x == 8:
            code += 'i'
        if x == 9:
            code += 'j'
        if x == 10:
            code += 'k'
        if x == 11:
            code += 'n'
        if x == 12:
            code += 'm'
        if x == 13:
            code += 'l'
        if x == 14:
            code += 'o'
        if x == 15:
            code += 'p'
        if x == 16:
            code += 'q'
        if x == 17:
            code += 'r'
        if x == 18:
            code += 's'
        if x == 19:
            code += 't'
        if x == 20:
            code += 'u'
        if x == 21:
            code += 'v'
        if x == 22:
            code += 'x'
        if x == 23:
            code += 'y'
        if x == 24:
            code += 'z'
        if x == 25:
            code += 'w'


    return(code)

def pin():
    f = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\pin_list_for_USER_code.txt', 'r')
    r = f.read()

    pin = '000000000'
    while(1):
        if pin in r:
            pin = str(int(pin)+1)
            pin = ('0'*(9-len(pin))) + pin
            continue
        else:
            break
    f.close()
    return(pin)


def ym():
    n = datetime.datetime.now()

    ym = ''
    ym += str(n.year)[2:]
    if len(str(n.month)) == 1:
        t = '0' + str(n.month)
    else:
        t = str(n.month)

    ym+=t
    return(ym)

        

def main():
    zip_code = input('Enter zip code : ')
    code = ran() + pin() + ym() + zip_code
    print('Code : ', code)
    ff = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\pin_list_for_USER_code.txt', 'a')
    ff.write((code + "\n"))
    ff.close()

if __name__ == '__main__':
    main()
