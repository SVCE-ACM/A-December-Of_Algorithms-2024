using System;

class Program
{
    static int CountRobotPaths(int[] steps, int distance)
    {
        if (distance == 0)
            return 1;

        int[] dp = new int[distance + 1];
        dp[0] = 1;

        for (int i = 1; i <= distance; i++)
        {
            foreach (int step in steps)
            {
                if (i - step >= 0)
                    dp[i] += dp[i - step];
            }
        }

        return dp[distance];
    }

    static void Main()
    {
        int[] steps = { 1, 2, 3 };
        int distance = 4;
        Console.WriteLine(CountRobotPaths(steps, distance));  // Example usage
    }
}
