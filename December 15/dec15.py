l=[]
w=int(input("Enter maximum capacity:"))
choice=1
n=0
while choice!=0:
    a = int(input("Enter number of gifts:"))
    l.append(a)
    n+=1
    choice = int(input("Do you want to continue?(0/1):"))
s=0
t=0
i=0
while i<n:
    s+=l[i]
    if s>w:
        t+=1
        s=l[i]
        
    i+=1

if s>0:
    t+=1
print("Number of trips required is:",t)
