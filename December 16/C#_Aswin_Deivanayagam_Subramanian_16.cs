using System;
using System.Linq;

class Program
{
    static int MinPlatforms(int[] arrivals, int[] departures)
    {
        Array.Sort(arrivals);
        Array.Sort(departures);
        
        int platformsNeeded = 0;
        int currentPlatforms = 0;

        int i = 0, j = 0;

        while (i < arrivals.Length)
        {
            if (arrivals[i] <= departures[j])
            {
                currentPlatforms++;
                i++;
            }
            else
            {
                currentPlatforms--;
                j++;
            }

            platformsNeeded = Math.Max(platformsNeeded, currentPlatforms);
        }

        return platformsNeeded;
    }

    static void Main()
    {
        int[] arrivals = { 100, 140, 150, 200 };
        int[] departures = { 110, 160, 170, 230 };
        Console.WriteLine(MinPlatforms(arrivals, departures));  // Example usage
    }
}
