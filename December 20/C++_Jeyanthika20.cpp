#include <iostream>
#include <vector>
using namespace std;

int countRobotPaths(vector<int>& steps, int distance) {
    vector<int> dp(distance + 1, 0);
    dp[0] = 1;

    for (int i = 1; i <= distance; i++) {
        for (int step : steps) {
            if (i - step >= 0) dp[i] += dp[i - step];
        }
    }

    return dp[distance];
}
