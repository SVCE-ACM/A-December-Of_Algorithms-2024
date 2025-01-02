#include <stdio.h>

int plantGrowthTracker(int n) {
    if (n == 1 || n == 2) {
        return 1;
    }

    int prev = 1, curr = 1, temp;
    for (int i = 3; i <= n; i++) {
        temp = curr;
        curr = prev + curr;
        prev = temp;
    }

    return curr;
}

int main() {
    // Test cases
    printf("%d\n", plantGrowthTracker(10));  // Output: 55
    printf("%d\n", plantGrowthTracker(12));  // Output: 144
    return 0;
}
