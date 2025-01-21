def compute_final_result(grid):
    N = len(grid)
    
    primary_diag_sum = 0
    secondary_diag_sum = 0
    for i in range(N):
        primary_diag_sum += grid[i][i]
        secondary_diag_sum += grid[i][N - 1 - i]
    
    diagonal_energy = abs(primary_diag_sum - secondary_diag_sum)
    
    boundary_energy = 0
    for i in range(N):
        boundary_energy += grid[0][i]
        boundary_energy += grid[N - 1][i]
    
    for i in range(1, N - 1):
        boundary_energy += grid[i][0]
        boundary_energy += grid[i][N - 1]
    
    final_result = diagonal_energy + boundary_energy
    return final_result

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(compute_final_result(grid))
