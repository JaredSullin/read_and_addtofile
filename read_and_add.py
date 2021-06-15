
def adduser():
    adduser = input("choice y/n")
    file = open("users.txt",'a')
    while adduser == 'y' or adduser == 'Y':
        name = input('what is your name')
        age = input('what is your age')
    else:
        print('name and age not added good bye')
        file.close()

def readuser ():
    readuser = input("choice y/n")
    file = open("users.txt",'r')
    while readuser == 'y' or readuser == 'Y':
        entirefile = file.read()
        print(entirefile)
    else:
        print('name and age shown good bye')
        file.close()
