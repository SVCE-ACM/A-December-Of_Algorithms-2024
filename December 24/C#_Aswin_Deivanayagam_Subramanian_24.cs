using System;
using System.Collections.Generic;

public class StringPermutationGrouping
{
    public static Dictionary<char, List<string>> GroupPermutations(string s)
    {
        var result = new Dictionary<char, List<string>>();
        var uniquePermutations = GetUniquePermutations(s.ToCharArray(), 0, s.Length - 1);

        foreach (var perm in uniquePermutations)
        {
            char firstLetter = perm[0];
            if (!result.ContainsKey(firstLetter))
            {
                result[firstLetter] = new List<string>();
            }
            result[firstLetter].Add(perm);
        }

        foreach (var key in result.Keys)
        {
            result[key].Sort();
        }

        return result;
    }

    private static HashSet<string> GetUniquePermutations(char[] array, int start, int end)
    {
        var result = new HashSet<string>();

        if (start == end)
        {
            result.Add(new string(array));
        }
        else
        {
            for (int i = start; i <= end; i++)
            {
                Swap(ref array[start], ref array[i]);
                var permutations = GetUniquePermutations(array, start + 1, end);
                foreach (var perm in permutations)
                {
                    result.Add(perm);
                }
                Swap(ref array[start], ref array[i]); // Backtrack
            }
        }

        return result;
    }

    private static void Swap(ref char a, ref char b)
    {
        char temp = a;
        a = b;
        b = temp;
    }

    public static void Main(string[] args)
    {
        string input = "abc";
        var result = GroupPermutations(input);

        foreach (var group in result)
        {
            Console.WriteLine($"{group.Key}: {string.Join(", ", group.Value)}");
        }
    }
}
