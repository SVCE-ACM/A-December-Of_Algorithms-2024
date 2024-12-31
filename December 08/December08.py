N = int(input())
totalString = ""
sum=0
for i in range(1,N+1):
    totalString+=str(i)
totalString=int(totalString)
while(totalString>0):
    temp=totalString%10
    sum+=temp**2
    totalString//=10
print(sum)