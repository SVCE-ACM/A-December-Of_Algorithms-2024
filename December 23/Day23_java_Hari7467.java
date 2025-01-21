public class Day23_java_Hari7467 {

    static int[][] grid = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    static int N = grid.length;

    static int calculateBoundarySum() {
        int sum = 0;
        for (int j = 0; j < N; j++) {
            sum += grid[0][j];
        }
        for (int i = 1; i < N - 1; i++) {
            sum += grid[i][N - 1];
        }
        for (int j = N - 1; j >= 0; j--) {
            sum += grid[N - 1][j];
        }
        for (int i = N - 2; i > 0; i--) {
            sum += grid[i][0];
        }
        return sum;
    }

    static int calculateDiagonalDifference() {
        int d1 = 0, d2 = 0;
        for (int i = 0; i < N; i++) {
            d1 += grid[i][i];
            d2 += grid[i][N - i - 1];
        }
        return Math.abs(d1 - d2);
    }

    public static void main(String[] args) {
        int boundarySum = calculateBoundarySum();
        int diagonalDifference = calculateDiagonalDifference();
        int finalResult = boundarySum + diagonalDifference;

        System.out.println("Final_Result = " + finalResult);
    }
}
