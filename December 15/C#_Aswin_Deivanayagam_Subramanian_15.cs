using System;
using System.Collections.Generic;

class Program
{
    static int MinTrips(List<int> houses, int W)
    {
        int trips = 0;
        int currentLoad = 0;

        foreach (int gifts in houses)
        {
            if (currentLoad + gifts > W)
            {
                trips++;
                currentLoad = 0;
            }
            currentLoad += gifts;
        }

        if (currentLoad > 0)
        {
            trips++;
        }

        return trips;
    }

    static void Main()
    {
        var houses = new List<int> { 5, 10, 7, 3, 6 };
        Console.WriteLine(MinTrips(houses, 15));  // Example usage
    }
}
