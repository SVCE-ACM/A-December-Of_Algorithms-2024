using System;

public class LavaFieldEscape
{
    public static bool CanJump(int[] nums)
    {
        int maxReach = 0;
        int n = nums.Length;

        for (int i = 0; i < n; i++)
        {
            if (i > maxReach)
                return false;

            maxReach = Math.Max(maxReach, i + nums[i]);

            if (maxReach >= n - 1)
                return true;
        }

        return false;
    }

    public static void Main(string[] args)
    {
        int[] nums1 = { 2, 3, 1, 0, 4 };
        int[] nums2 = { 3, 2, 1, 0, 4 };

        Console.WriteLine(CanJump(nums1)); // Output: True
        Console.WriteLine(CanJump(nums2)); // Output: False
    }
}
