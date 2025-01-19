//(31) Speed of Light Simulation:
#include <stdio.h>
#include <math.h>

#define EPSILON 1e-6

float fast_inv_sqrt(float x) {
    long i = *(long*)&x;
    i = 0x5f3759df - (i >> 1);
    x = *(float*)&i;
    return x * (1.5f - 0.5f * x * x);
}

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int x, y, z;
        scanf("%d %d %d", &x, &y, &z);
        float magnitude = sqrtf(x * x + y * y + z * z);
        if (magnitude < EPSILON) {
            printf("0.000000 0.000000 0.000000\n");
        } else {
            float inv_mag = fast_inv_sqrt(x * x + y * y + z * z);
            printf("%.6f %.6f %.6f\n", x * inv_mag, y * inv_mag, z * inv_mag);
        }
    }
    return 0;
}

