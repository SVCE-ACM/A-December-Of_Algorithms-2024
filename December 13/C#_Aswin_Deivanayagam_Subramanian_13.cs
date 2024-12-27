using System;
using System.Collections.Generic;

class Program
{
    static int MinSwaps(List<int> nums)
    {
        var sortedNums = new List<int>(nums);
        sortedNums.Sort();
        var pos = new Dictionary<int, int>();
        
        for (int i = 0; i < sortedNums.Count; i++)
        {
            pos[sortedNums[i]] = i;
        }

        int count = 0;
        
        for (int i = 0; i < nums.Count; i++)
        {
            if (pos[nums[i]] != i)
            {
                count++;
                int temp = nums[i];
                nums[i] = nums[pos[nums[i]]];
                nums[pos[nums[i]]] = temp;
                pos[nums[i]] = i;
            }
        }

        return count;
    }

    static void Main()
    {
        var nums = new List<int> { 4, 3, 2, 1 };
        Console.WriteLine(MinSwaps(nums));  // Example usage
    }
}
