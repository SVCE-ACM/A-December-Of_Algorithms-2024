numRows = int(input())
tower = []
for _ in range(2):
    row = input().strip()
    tower.append([int(x) for x in row.strip("[]").split(",")])
for i in range(2,numRows):
    temp = [1]
    for j in range(len(tower[i-1])-1):
        temp.append(tower[i-1][j]+tower[i-1][j+1])
    temp.append(1)
    tower.append(temp)
print(tower)
