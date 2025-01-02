using System;

class Program
{
    static int Josephus(int n, int k)
    {
        int safePosition = 0;
        for (int i = 1; i <= n; i++)
        {
            safePosition = (safePosition + k) % i;
        }
        return safePosition + 1;
    }

    static void Main()
    {
        Console.WriteLine(Josephus(3, 2));
        Console.WriteLine(Josephus(5, 3));
    }
}
