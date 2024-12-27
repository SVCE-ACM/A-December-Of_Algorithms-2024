using System;

class Program
{
    static int FindMissingNumber(int N, int[] array)
    {
        int expectedSum = N * (N + 1) / 2;
        int actualSum = 0;
        
        foreach (int num in array)
        {
            actualSum += num;
        }
        
        return expectedSum - actualSum;
    }

    static void Main()
    {
        // Test cases
        Console.WriteLine(FindMissingNumber(5, new int[] { 1, 2, 4, 5 }));  // Output: 3
        Console.WriteLine(FindMissingNumber(3, new int[] { 1, 3 }));        // Output: 2
    }
}
