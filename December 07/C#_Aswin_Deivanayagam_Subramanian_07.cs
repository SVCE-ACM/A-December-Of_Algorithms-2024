using System;
using System.Collections.Generic;

class Program
{
    static List<List<int>> GeneratePascalTriangle(int numRows)
    {
        List<List<int>> result = new List<List<int>>();

        if (numRows == 0)
        {
            return result;
        }

        result.Add(new List<int> { 1 });

        for (int i = 1; i < numRows; i++)
        {
            List<int> row = new List<int> { 1 };

            for (int j = 1; j < i; j++)
            {
                row.Add(result[i - 1][j - 1] + result[i - 1][j]);
            }

            row.Add(1);
            result.Add(row);
        }

        return result;
    }

    static void Main()
    {
        var triangle = GeneratePascalTriangle(5);
        foreach (var row in triangle)
        {
            Console.WriteLine(string.Join(" ", row));
        }
    }
}
