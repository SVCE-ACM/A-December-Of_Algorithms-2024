def pascal_tower(n):
    if n <= 0:
        print("Please enter a positive number for the floors.")
        return
    tower = []

    for i in range(n):
        floor = [1] * (i + 1)
        for j in range(1, i):
            floor[j] = tower[i - 1][j - 1] + tower[i - 1][j]
        tower.append(floor)
    print("Magical Tower with", n, "floors:")
    print(tower)
n = int(input("Enter the number of floors for the Magical Tower: "))
pascal_tower(n)
