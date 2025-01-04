//(23) Crystal Grid
#include <stdio.h>
#include <stdlib.h>

int main() {
    int N;
    scanf("%d", &N);
    
    int grid[N][N];
    int primary_diag = 0, secondary_diag = 0, boundary_sum = 0;
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &grid[i][j]);
            if (i == j) primary_diag += grid[i][j];
            if (i + j == N - 1) secondary_diag += grid[i][j];
            if (i == 0 || i == N - 1 || j == 0 || j == N - 1) boundary_sum += grid[i][j];
        }
    }
    
    int diagonal_energy = abs(primary_diag - secondary_diag);
    int final_result = diagonal_energy + boundary_sum;
    
    printf("%d\n", final_result);
    return 0;
}

