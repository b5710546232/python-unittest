
def stamp7(tempMoney):
    stamps = {"stamp_1":0,"stamp_3":0}
    while(tempMoney>=40):
        if(tempMoney>=120):
            # give stamp 3 b
            stamps["stamp_3"] += 1
            tempMoney -=120
        elif (tempMoney>=40):
            # give stamp 1 b
            stamps["stamp_1"] += 1
            tempMoney -=40
    return stamps

def memberCheck(memberID):
    if (memberID == '1234'):
        return True
    else :
        return False

def main():
    inputId = input("input Id :")
    if(memberCheck(inputId)):
        print('You are a member')
    else:
        print('You are a not member')
    
    money = input('Input money :')
    money = int(money)
    tempMoney = money
    
    for item in stamp7(tempMoney):
        print(item,'=',stamp7(tempMoney)[item])


if __name__ == '__main__':
    main()