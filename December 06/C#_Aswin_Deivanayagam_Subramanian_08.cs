using System;

class Program
{
    static int DigitSquareSum(int N)
    {
        int DigitSquareSumOfNumber(int num)
        {
            int total = 0;
            while (num > 0)
            {
                int digit = num % 10;
                total += digit * digit;
                num /= 10;
            }
            return total;
        }

        int totalSum = 0;
        for (int i = 1; i <= N; i++)
        {
            totalSum += DigitSquareSumOfNumber(i);
        }
        return totalSum;
    }

    static void Main()
    {
        Console.WriteLine(DigitSquareSum(10));  // Example usage
    }
}
