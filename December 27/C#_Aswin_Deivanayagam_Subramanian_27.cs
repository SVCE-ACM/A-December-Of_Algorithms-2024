using System;

public class TrappingRainWater
{
    public static int Trap(int[] height)
    {
        int n = height.Length;
        if (n == 0) return 0;

        int leftMax = 0, rightMax = 0;
        int left = 0, right = n - 1;
        int waterTrapped = 0;

        while (left < right)
        {
            if (height[left] < height[right])
            {
                if (height[left] >= leftMax)
                {
                    leftMax = height[left];
                }
                else
                {
                    waterTrapped += leftMax - height[left];
                }
                left++;
            }
            else
            {
                if (height[right] >= rightMax)
                {
                    rightMax = height[right];
                }
                else
                {
                    waterTrapped += rightMax - height[right];
                }
                right--;
            }
        }

        return waterTrapped;
    }

    public static void Main(string[] args)
    {
        int[] height1 = { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 };
        int[] height2 = { 4, 2, 0, 3, 2, 5 };

        Console.WriteLine(Trap(height1)); // Output: 6
        Console.WriteLine(Trap(height2)); // Output: 9
    }
}
