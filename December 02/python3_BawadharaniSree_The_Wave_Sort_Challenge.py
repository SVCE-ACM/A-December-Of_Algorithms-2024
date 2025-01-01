arr=list(map(int,input().split()))
for i in range(len(arr)-1):
   if(i%2==0):
      if (arr[i]<arr[i+1]):
         arr[i],arr[i+1]=arr[i+1],arr[i]
   elif (arr[i]>arr[i+1]):
      arr[i],arr[i+1]=arr[i+1],arr[i]
print(arr)