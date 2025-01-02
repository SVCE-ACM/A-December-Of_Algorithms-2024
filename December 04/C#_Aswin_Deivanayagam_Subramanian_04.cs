using System;

class Program
{
    static int PlantGrowthTracker(int n)
    {
        if (n == 1 || n == 2)
        {
            return 1;
        }

        int prev = 1, curr = 1;
        for (int i = 3; i <= n; i++)
        {
            int temp = curr;
            curr = prev + curr;
            prev = temp;
        }

        return curr;
    }

    static void Main()
    {
        Console.WriteLine(PlantGrowthTracker(10));
        Console.WriteLine(PlantGrowthTracker(12));
    }
}
