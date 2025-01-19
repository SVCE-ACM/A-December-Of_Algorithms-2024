//(18) Howard's Rare Gems:
#include <stdio.h>
#include <string.h>

int get_value(char gem) {
    if (gem == 'D') return 500;
    if (gem == 'R') return 250;
    if (gem == 'E') return 100;
    return 0;
}

int max_profit(char* chain) {
    int n = strlen(chain);
    int max_len = 1, max_profit = 0;
    int dp[2][n];
    memset(dp, 0, sizeof(dp));
    
    for (int i = 0; i < n; i++) {
        dp[0][i] = get_value(chain[i]);
        for (int len = 2; len <= n - i; len++) {
            int j = i + len - 1;
            if (chain[i] == chain[j]) {
                dp[len % 2][j] = dp[(len - 1) % 2][j - 1] + get_value(chain[j]);
                int profit = dp[len % 2][j] * len;
                if (profit > max_profit) max_profit = profit;
            }
        }
    }
    return max_profit;
}

int main() {
    char chain1[] = "RDEREDRRRD";
    char chain2[] = "DERRREDERREDEREDR";
    printf("%d\n", max_profit(chain1));
    printf("%d\n", max_profit(chain2));
    return 0;
}

