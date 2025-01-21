import java.util.ArrayList;
import java.util.List;

class VectorNormalization {

    public static float fastInverseSqrt(float x) {
        float halfX = 0.5f * x;
        int i = Float.floatToIntBits(x);
        i = 0x5f3759df - (i >> 1);
        x = Float.intBitsToFloat(i);
        x *= (1.5f - halfX * x * x); // Newton's method refinement
        return x;
    }

    public static List<float[]> normalizeVectors(List<float[]> vectors) {
        List<float[]> normalizedVectors = new ArrayList<>();
        for (float[] vec : vectors) {
            float x = vec[0], y = vec[1], z = vec[2];
            float magnitudeSquared = x * x + y * y + z * z;
            float invMagnitude = fastInverseSqrt(magnitudeSquared);
            normalizedVectors.add(new float[]{x * invMagnitude, y * invMagnitude, z * invMagnitude});
        }
        return normalizedVectors;
    }

    public static void main(String[] args) {
        List<float[]> vectors = new ArrayList<>();
        vectors.add(new float[]{3, 4, 0});
        vectors.add(new float[]{-6, 8, 0});
        vectors.add(new float[]{5, 12, 0});

        List<float[]> normalizedVectors = normalizeVectors(vectors);

        for (float[] vec : normalizedVectors) {
            System.out.printf("%.6f %.6f %.6f%n", vec[0], vec[1], vec[2]);
        }
    }
}
