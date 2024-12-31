N = int(input('Enter size : '))
arr = list(map(int,input().split()))
total = (N *( N + 1 )) // 2
print("Missing Number : ",total - sum(arr))