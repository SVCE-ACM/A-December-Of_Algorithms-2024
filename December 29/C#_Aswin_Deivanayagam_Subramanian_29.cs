using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static int MinWeightToExit(int N, int M, int P, List<(int, int, int, int, int)> portals)
    {
        var graph = new Dictionary<(int, int), List<((int, int), int)>>();

        foreach (var portal in portals)
        {
            var (x1, y1, x2, y2, W) = portal;
            if (!graph.ContainsKey((x1, y1)))
                graph[(x1, y1)] = new List<((int, int), int)>();
            if (!graph.ContainsKey((x2, y2)))
                graph[(x2, y2)] = new List<((int, int), int)>();
            
            graph[(x1, y1)].Add(((x2, y2), W));
            graph[(x2, y2)].Add(((x1, y1), W));
        }

        var pq = new SortedSet<(int Weight, int X, int Y)>(Comparer<(int Weight, int X, int Y)>.Create((a, b) => 
        {
            if (a.Weight != b.Weight) return a.Weight.CompareTo(b.Weight);
            if (a.X != b.X) return a.X.CompareTo(b.X);
            return a.Y.CompareTo(b.Y);
        }));
        
        pq.Add((0, 1, 1));
        var visited = new HashSet<(int, int)>();

        while (pq.Count > 0)
        {
            var current = pq.Min;
            pq.Remove(current);

            var (currWeight, x, y) = current;
            if (visited.Contains((x, y)))
                continue;

            visited.Add((x, y));

            if ((x, y) == (N, M))
                return currWeight;

            foreach (var (dx, dy) in new[] { (-1, 0), (1, 0), (0, -1), (0, 1) })
            {
                int nx = x + dx, ny = y + dy;
                if (nx >= 1 && nx <= N && ny >= 1 && ny <= M && !visited.Contains((nx, ny)))
                {
                    pq.Add((currWeight, nx, ny));
                }
            }

            if (graph.ContainsKey((x, y)))
            {
                foreach (var ((nx, ny), w) in graph[(x, y)])
                {
                    if (!visited.Contains((nx, ny)))
                    {
                        pq.Add((currWeight + w, nx, ny));
                    }
                }
            }
        }

        return -1;
    }

    static void Main(string[] args)
    {
        var input = Console.ReadLine().Split();
        int N = int.Parse(input[0]);
        int M = int.Parse(input[1]);
        int P = int.Parse(Console.ReadLine());
        var portals = new List<(int, int, int, int, int)>();

        for (int i = 0; i < P; i++)
        {
            var portalInput = Console.ReadLine().Split().Select(int.Parse).ToArray();
            portals.Add((portalInput[0], portalInput[1], portalInput[2], portalInput[3], portalInput[4]));
        }

        Console.WriteLine(MinWeightToExit(N, M, P, portals));
    }
}
