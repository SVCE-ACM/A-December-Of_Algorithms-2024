using System;
using System.Collections.Generic;

class Program
{
    static List<Tuple<int, int>> TargetPairFinder(int[] numbers, int target)
    {
        List<Tuple<int, int>> uniquePairs = new List<Tuple<int, int>>();
        HashSet<int> seen = new HashSet<int>();

        foreach (int num in numbers)
        {
            int complement = target - num;
            if (seen.Contains(complement))
            {
                uniquePairs.Add(new Tuple<int, int>(complement, num));
            }
            else
            {
                seen.Add(num);
            }
        }

        return uniquePairs;
    }

    static void Main()
    {
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
