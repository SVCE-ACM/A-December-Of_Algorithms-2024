using System;
using System.Text;

class Program
{
    static string AlternatingSquareArrangement(int R, int B)
    {
        if (Math.Abs(R - B) > 1)
        {
            return "Not possible";
        }

        StringBuilder result = new StringBuilder();
        int major = R >= B ? R : B;
        int minor = R >= B ? B : R;
        char majorColor = R >= B ? 'R' : 'B';
        char minorColor = R >= B ? 'B' : 'R';

        for (int i = 0; i < major + minor; i++)
        {
            if (major > 0)
            {
                result.Append(majorColor);
                major--;
            }
            if (minor > 0 && (result.Length == 0 || result[result.Length - 1] == majorColor))
            {
                result.Append(minorColor);
                minor--;
            }
        }

        return result.ToString();
    }

    static void Main()
    {
        Console.WriteLine(AlternatingSquareArrangement(3, 2));
        Console.WriteLine(AlternatingSquareArrangement(4, 2));
    }
}
