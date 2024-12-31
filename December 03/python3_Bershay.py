def validSequence():
    R = int(input('Enter Red : '))
    B = int(input('Enter Blue : '))
    lastString = 'R' if R > B else 'B' if R < B else ''
    flag = 1 if R > B else 0
    if(abs(R - B)>1 or R<=0 and B<=0):
        print('Not Possible')
    else:
        for i in range(min(R,B)):
            if(flag):
                print('RB',end="")
            elif(not flag):
                print('BR',end="")
        print(lastString)        
    
if __name__=='__main__':
    validSequence()    
    
