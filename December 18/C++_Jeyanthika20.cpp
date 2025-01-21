#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int gemValue(char gem) {
    if (gem == 'D') return 500;
    if (gem == 'R') return 250;
    if (gem == 'E') return 100;
    return 0;
}

int maxPalindromicChainProfit(string chain) {
    int n = chain.size();
    if (n == 0) return 0;

    string s = "@#" + string(chain.begin(), chain.end()) + "#$";
    vector<int> p(s.size(), 0);
    int c = 0, r = 0;

    for (int i = 1; i < s.size() - 1; i++) {
        if (i < r) p[i] = min(r - i, p[2 * c - i]);
        while (s[i + p[i] + 1] == s[i - p[i] - 1]) p[i]++;
        if (i + p[i] > r) {
            c = i;
            r = i + p[i];
        }
    }

    int maxLen = 0, center = 0;
    for (int i = 1; i < s.size() - 1; i++) {
        if (p[i] > maxLen) {
            maxLen = p[i];
            center = i;
        }
    }

    int start = (center - maxLen) / 2;
    int end = (center + maxLen) / 2;

    int totalValue = 0;
    for (int i = start; i <= end; i++) {
        totalValue += gemValue(chain[i]);
    }

    return totalValue * (end - start + 1);
}
