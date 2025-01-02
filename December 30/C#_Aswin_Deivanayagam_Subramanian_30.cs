using System;

class Program
{
    public static int SuperEggDrop(int k, int n)
    {
        int[,] dp = new int[k + 1, n + 1];

        for (int moves = 1; moves <= n; moves++)
        {
            for (int eggs = 1; eggs <= k; eggs++)
            {
                dp[eggs, moves] = dp[eggs - 1, moves - 1] + dp[eggs, moves - 1] + 1;
                if (dp[eggs, moves] >= n)
                {
                    return moves;
                }
            }
        }

        return 0;
    }

    static void Main()
    {
        Console.WriteLine(SuperEggDrop(2, 6));  // Output: 3
        Console.WriteLine(SuperEggDrop(3, 14)); // Output: 4
    }
}
