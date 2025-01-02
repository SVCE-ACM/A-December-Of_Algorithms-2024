using System;

class Program
{
    static double CalculateDistance(int x1, int y1, int x2, int y2)
    {
        return Math.Sqrt(Math.Pow(x1 - x2, 2) + Math.Pow(y1 - y2, 2));
    }

    static int EarthquakePropagation(int[,] buildings)
    {
        int maxAffected = 0;

        for (int i = 0; i < buildings.GetLength(0); i++)
        {
            int affected = 1;
            for (int j = 0; j < buildings.GetLength(0); j++)
            {
                if (i != j)
                {
                    double distance = CalculateDistance(buildings[i, 0], buildings[i, 1], buildings[j, 0], buildings[j, 1]);
                    if (distance <= buildings[i, 2])
                    {
                        affected++;
                    }
                }
            }
            maxAffected = Math.Max(maxAffected, affected);
        }

        return maxAffected;
    }

    static void Main()
    {
        int[,] buildings = {
            { 2, 1, 3 },
            { 6, 1, 4 }
        };

        int maxAffected = EarthquakePropagation(buildings);
        Console.WriteLine(maxAffected);
    }
}
