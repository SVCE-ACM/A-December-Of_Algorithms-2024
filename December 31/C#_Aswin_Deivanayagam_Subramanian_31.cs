using System;

class Program
{
    public static float FastInverseSqrt(float x)
    {
        float threeHalfs = 1.5f;
        float x2 = x * 0.5f;
        int i = BitConverter.ToInt32(BitConverter.GetBytes(x), 0);
        i = 0x5f3759df - (i >> 1);
        float y = BitConverter.ToSingle(BitConverter.GetBytes(i), 0);
        y = y * (threeHalfs - (x2 * y * y));
        return y;
    }

    public static (float, float, float)[] NormalizeVectors((float, float, float)[] vectors)
    {
        (float, float, float)[] result = new (float, float, float)[vectors.Length];
        for (int i = 0; i < vectors.Length; i++)
        {
            var vec = vectors[i];
            float x = vec.Item1, y = vec.Item2, z = vec.Item3;
            float magnitudeSquared = x * x + y * y + z * z;
            float invMagnitude = FastInverseSqrt(magnitudeSquared);
            result[i] = (x * invMagnitude, y * invMagnitude, z * invMagnitude);
        }
        return result;
    }

    static void Main()
    {
        var vectors = new (float, float, float)[]
        {
            (3, 4, 0),
            (-6, 8, 0),
            (5, 12, 0)
        };

        var normalizedVectors = NormalizeVectors(vectors);
        foreach (var vec in normalizedVectors)
        {
            Console.WriteLine($"{vec.Item1:F6} {vec.Item2:F6} {vec.Item3:F6}");
        }
    }
}
