using System;
using System.Collections.Generic;

class Program
{
    static List<Tuple<string, string>> TowerOfHanoi(int n, string source, string destination, string auxiliary)
    {
        if (n == 0)
            return new List<Tuple<string, string>>();

        var moves = new List<Tuple<string, string>>();
        moves.AddRange(TowerOfHanoi(n - 1, source, auxiliary, destination));
        moves.Add(Tuple.Create(source, destination));
        moves.AddRange(TowerOfHanoi(n - 1, auxiliary, destination, source));

        return moves;
    }

    static void Main()
    {
        int numDisks = 4;
        string start = "A";
        string destination = "C";
        string auxiliary = "B";

        var moves = TowerOfHanoi(numDisks, start, destination, auxiliary);

        Console.WriteLine($"Minimum number of moves: {moves.Count}");
        Console.WriteLine("Sequence of moves:");
        for (int i = 0; i < moves.Count; i++)
        {
            Console.WriteLine($"{i + 1}. Move disk 1 from {moves[i].Item1} to {moves[i].Item2}");
        }
    }
}
