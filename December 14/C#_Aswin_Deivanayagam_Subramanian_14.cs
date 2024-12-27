using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static string CanSplitSquad(int N, int K, int D, List<int> A)
    {
        var subjectCounts = A.GroupBy(x => x).ToDictionary(g => g.Key, g => g.Count());
        int uniqueSubjects = subjectCounts.Count;

        if (uniqueSubjects < K)
        {
            return "NO";
        }

        int maxTeamSize = (N + D) / 2;
        int minTeamSize = (N - D) / 2;

        if (subjectCounts.Values.Count(count => count <= minTeamSize) < K)
        {
            return "NO";
        }

        return "YES";
    }

    static void Main()
    {
        var A = new List<int> { 1, 2, 2, 3, 3, 4, 4 };
        Console.WriteLine(CanSplitSquad(7, 3, 2, A));  // Example usage
    }
}
