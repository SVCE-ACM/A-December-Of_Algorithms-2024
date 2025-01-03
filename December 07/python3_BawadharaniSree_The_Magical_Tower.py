def generate_magical_tower(numRows):
    tower = []
    for i in range(numRows):
        floor = [1]
        for j in range(1, i):
            floor.append(tower[i-1][j-1] + tower[i-1][j])
        if i > 0:
            floor.append(1)
        tower.append(floor)
    return tower

numRows = int(input("Enter the number of floors (numRows): "))
tower = generate_magical_tower(numRows)
print("The Magical Tower:", tower)