using System;

class Program
{
    static int CrystalGridFinalResult(int[,] grid)
    {
        int n = grid.GetLength(0);
        int primarySum = 0, secondarySum = 0, boundarySum = 0;

        for (int i = 0; i < n; i++)
        {
            primarySum += grid[i, i];
            secondarySum += grid[i, n - 1 - i];
            for (int j = 0; j < n; j++)
            {
                if (i == 0 || i == n - 1 || j == 0 || j == n - 1)
                {
                    boundarySum += grid[i, j];
                }
            }
        }

        int diagonalEnergy = Math.Abs(primarySum - secondarySum);
        int finalResult = diagonalEnergy + boundarySum;
        return finalResult;
    }

    static void Main()
    {
        int[,] grid = {
            { 1, 2, 3 },
            { 4, 5, 6 },
            { 7, 8, 9 }
        };

        int result = CrystalGridFinalResult(grid);
        Console.WriteLine(result);  // Output: 40
    }
}
