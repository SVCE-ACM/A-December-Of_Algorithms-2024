returns = list(map(int, input().split()))
result = max(set(returns), key=returns.count)
count = 0
for i in returns:
    if(i==1):
        count+=1
print(count)
