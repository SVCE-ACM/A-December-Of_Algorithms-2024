def calculate_crystal_grid(grid):
    n = len(grid)

    # Calculate the primary and secondary diagonal sums
    primary_diagonal_elements = [grid[i][i] for i in range(n)]
    secondary_diagonal_elements = [grid[i][n - i - 1] for i in range(n)]
    primary_diagonal_sum = sum(primary_diagonal_elements)
    secondary_diagonal_sum = sum(secondary_diagonal_elements)

    # Diagonal energy difference
    diagonal_energy = abs(primary_diagonal_sum - secondary_diagonal_sum)

    # Calculate boundary energy
    boundary_elements = []
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                boundary_elements.append(grid[i][j])
    boundary_energy = sum(boundary_elements)

    # Final result
    final_result = diagonal_energy + boundary_energy

    # Print details
    print("Diagonal Energy Difference:")
    print(f"Primary Diagonal = {' + '.join(map(str, primary_diagonal_elements))} = {primary_diagonal_sum}")
    print(f"Secondary Diagonal = {' + '.join(map(str, secondary_diagonal_elements))} = {secondary_diagonal_sum}")
    print(f"Diagonal_Energy = |{primary_diagonal_sum} - {secondary_diagonal_sum}| = {diagonal_energy}")
    print("Boundary Energy:")
    print(f"Boundary elements = {', '.join(map(str, boundary_elements))}")
    print(f"Boundary_Energy = {' + '.join(map(str, boundary_elements))} = {boundary_energy}")
    print("Final Magical Result:")
    print(f"Final_Result = Diagonal_Energy + Boundary_Energy = {diagonal_energy} + {boundary_energy} = {final_result}")

    return final_result

# Input grid from the user
n = int(input("Enter the size of the grid (N): "))
print("Enter the grid values row by row:")
grid = [list(map(int, input().split())) for _ in range(n)]

calculate_crystal_grid(grid)
