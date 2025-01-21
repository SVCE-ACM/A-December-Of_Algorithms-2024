public class Day31_java_Hari7467 {
        public static void main(String[] args) {
            float[][] velocities = {
                    {3, 4, 0},
                    {-6, 8, 0},
                    {5, 12, 0}
            };
            System.out.println("Normalized velocity vectors:");
            for (float[] velocity : velocities) {
                float[] normalized = normalizeVelocity(velocity);
                System.out.printf("Normalized: %.6f %.6f %.6f%n", normalized[0], normalized[1], normalized[2]);
            }
        }
      
        public static float[] normalizeVelocity(float[] velocity) {
            float squaredMagnitude = velocity[0] * velocity[0] 
                                   + velocity[1] * velocity[1] 
                                   + velocity[2] * velocity[2];

            float reciprocalSqrt = fastInverseSqrt(squaredMagnitude);
    
            return new float[] {
                    velocity[0] * reciprocalSqrt,
                    velocity[1] * reciprocalSqrt,
                    velocity[2] * reciprocalSqrt
            };
        }
        public static float fastInverseSqrt(float number) {
            int bits = Float.floatToIntBits(number);             
            int magic = 0x5f3759df;                              
            int approxBits = magic - (bits >> 1);                
            float approx = Float.intBitsToFloat(approxBits);     
            approx = approx * (1.5f - 0.5f * number * approx * approx);
            return approx;
        }
    }
    