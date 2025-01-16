#include <iostream>
#include <vector>
using namespace std;

int countPermutations(vector<int>& steps, int distance) {
    // Create a DP array initialized to 0
    
    vector<int> dp(distance + 1, 0);
    
    // Base case: 1 way to reach distance 0
    dp[0] = 1;
    
    // Fill the DP array
    for (int j = 1; j <= distance; j++) {
        for (int s : steps) {
            if (j >= s) {
                dp[j] += dp[j - s];
            }
            
        }
        cout<<"\n";
        cout<<j<<"\n";
        for(int s:dp){
            cout<<s<<" ";
        }
    }
    
    return dp[distance];
}

int main() {
    vector<int> steps = {1, 2, 3}; // Example step sizes
    int distance = 4;             // Example target distance
    
    cout << "Number of distinct ways: " << countPermutations(steps, distance) << endl;
    return 0;
}
