def GenMagicalTower(n):
    tower = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):  
            row[j] = tower[i-1][j-1] + tower[i-1][j]
        tower.append(row)    
    return tower

print(f"Resultant Tower: {GenMagicalTower(int(input('Enter No.Of Floors: ')))}")
