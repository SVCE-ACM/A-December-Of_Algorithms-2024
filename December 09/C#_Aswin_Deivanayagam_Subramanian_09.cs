using System;
using System.Linq;

class Program
{
    static int CountCustomersWithOneReturn(int[] returns)
    {
        return returns.Count(r => r == 1);
    }

    static void Main()
    {
        Console.WriteLine(CountCustomersWithOneReturn(new int[] { 1, 2, 1, 3, 1 }));  // Example usage
    }
}
