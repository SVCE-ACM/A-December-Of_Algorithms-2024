def calculateFinalResult(grid):
    N = len(grid)
    primary_sum = 0
    secondary_sum = 0
    for i in range(N):
        primary_sum += grid[i][i]
        secondary_sum += grid[i][N - 1 - i]
    diagonal_energy = abs(primary_sum - secondary_sum)
    boundary_energy = 0
    for i in range(N):
        boundary_energy += grid[0][i]
        boundary_energy += grid[N - 1][i]
    for i in range(1, N - 1):
        boundary_energy += grid[i][0]
        boundary_energy += grid[i][N - 1]
    final_result = diagonal_energy + boundary_energy
    return final_result

N = int(input())
grid = []
for i in range(N):
    grid.append(list(map(int, input().split())))

print(calculateFinalResult(grid))
