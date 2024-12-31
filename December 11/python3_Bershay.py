moves =input()
horizontal,vertical = 0,0
for i in moves:
    if(i=="U"):
        vertical+=1
    elif(i=="D"):
        vertical-=1
    elif(i=="L"):
        horizontal+=1
    elif(i=="R"):
        horizontal-=1
print(horizontal == 0 and vertical==0)
