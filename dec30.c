//(30) Super Egg Drop
#include <stdio.h>
#include <stdlib.h>

#define MAX 101

int dp[MAX][MAX];

int min(int a, int b) {
    return a < b ? a : b;
}

int superEggDrop(int k, int n) {
    for (int i = 0; i <= k; i++) {
        dp[i][0] = 0;
        dp[i][1] = 1;
    }
    for (int i = 0; i <= n; i++) {
        dp[1][i] = i;
    }
    for (int i = 2; i <= k; i++) {
        for (int j = 2; j <= n; j++) {
            dp[i][j] = MAX;
            for (int x = 1; x <= j; x++) {
                int res = 1 + max(dp[i-1][x-1], dp[i][j-x]);
                dp[i][j] = min(dp[i][j], res);
            }
        }
    }
    return dp[k][n];
}

int main() {
    int k, n;
    scanf("%d %d", &k, &n);
    printf("%d\n", superEggDrop(k, n));
    return 0;
}

