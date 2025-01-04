//(20) Robot Pathways Problem
#include <stdio.h>

int count_ways(int* steps, int n, int distance) {
    int dp[distance + 1];
    dp[0] = 1;
    for (int i = 1; i <= distance; i++) {
        dp[i] = 0;
        for (int j = 0; j < n; j++) {
            if (i - steps[j] >= 0) {
                dp[i] += dp[i - steps[j]];
            }
        }
    }
    return dp[distance];
}

int main() {
    int steps[] = {1, 2, 3};
    int distance = 4;
    int n = sizeof(steps) / sizeof(steps[0]);
    printf("%d\n", count_ways(steps, n, distance));
    return 0;
}

