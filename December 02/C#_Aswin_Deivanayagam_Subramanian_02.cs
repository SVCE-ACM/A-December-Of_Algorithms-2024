using System;

class Program
{
    static int[] WaveSort(int[] arr)
    {
        Array.Sort(arr);
        for (int i = 0; i < arr.Length - 1; i += 2)
        {
            int temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
        }
        return arr;
    }

    static void Main()
    {
        int[] result1 = WaveSort(new int[] { 10, 5, 6, 3, 2, 20, 100, 80 });
        Console.WriteLine(string.Join(", ", result1));

        int[] result2 = WaveSort(new int[] { 1, 2, 3, 4, 5, 6 });
        Console.WriteLine(string.Join(", ", result2));
    }
}
