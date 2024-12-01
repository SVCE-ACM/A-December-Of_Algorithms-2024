print(f"Missing Player: {int((lambda n: n*(n+1)/2 - sum(map(int, input('Enter Players: ').split())))(int(input('Enter No.Of Players: '))))}")
