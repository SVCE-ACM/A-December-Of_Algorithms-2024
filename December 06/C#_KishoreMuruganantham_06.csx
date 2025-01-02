using System;
using System.Collections.Generic;

class Program
{
    static List<(int, int)> TargetPairFinder(int[] numbers, int target)
    {
        List<(int, int)> uniquePairs = new List<(int, int)>();
        HashSet<int> seen = new HashSet<int>();

        foreach (int num in numbers)
        {
            int complement = target - num;
            if (!seen.Contains(complement))
            {
                seen.Add(num);
            }
            else
            {
                uniquePairs.Add((complement, num));
            }
        }

        return uniquePairs;
    }

    static void Main()
    {
        // Test cases
        var result1 = TargetPairFinder(new int[] { 2, 4, 3, 7, 1, 5 }, 6);
        foreach (var pair in result1)
        {
            Console.WriteLine($"({pair.Item1}, {pair.Item2})");
        }

        var result2 = TargetPairFinder(new int[] { 10, 15, 3, 7, 8, 12, 5 }, 20);
        foreach (var pair in result2)
        {
            Console.WriteLine($"({pair.Item1}, {pair.Item2})");
        }
    }
}
