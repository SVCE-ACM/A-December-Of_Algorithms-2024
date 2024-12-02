Arr = list(map(int,input("Enter A List: ").split(" ")))
for i in range(0,len(Arr)-1,2):
    if i+1 < len(Arr) and Arr[i] < Arr[i+1]:
        Arr[i],Arr[i+1] = Arr[i+1], Arr[i]
    if i+2<len(Arr) and Arr[i+1]>Arr[i+2]:
        Arr[i+1], Arr[i+2] = Arr[i+2], Arr[i+1]

print(Arr)
