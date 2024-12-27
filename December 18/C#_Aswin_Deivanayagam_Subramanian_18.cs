using System;
using System.Linq;

class Program
{
    static int GemValue(char gem)
    {
        switch (gem)
        {
            case 'D': return 500;
            case 'R': return 250;
            case 'E': return 100;
            default: return 0;
        }
    }

    static int MaxPalindromicChainProfit(string chain)
    {
        int n = chain.Length;
        if (n == 0)
            return 0;

        string s = "@#" + string.Join("#", chain.Select(c => c.ToString())) + "#$";
        int[] p = new int[s.Length];
        int c = 0, r = 0;

        for (int i = 1; i < s.Length - 1; i++)
        {
            if (i < r)
                p[i] = Math.Min(r - i, p[2 * c - i]);
            while (s[i + p[i] + 1] == s[i - p[i] - 1])
                p[i]++;
            if (i + p[i] > r)
            {
                c = i;
                r = i + p[i];
            }
        }

        int maxLength = 0;
        int center = 0;
        for (int i = 1; i < s.Length - 1; i++)
        {
            if (p[i] > maxLength)
            {
                maxLength = p[i];
                center = i;
            }
        }

        int start = (center - maxLength) / 2;
        int end = (center + maxLength) / 2;

        int totalValue = 0;
        for (int i = start; i < end; i++)
        {
            totalValue += GemValue(chain[i]);
        }

        int profit = totalValue * (end - start + 1);

        return profit;
    }

    static void Main()
    {
        string chain = "DRREED";
        Console.WriteLine(MaxPalindromicChainProfit(chain));  // Example usage
    }
}
