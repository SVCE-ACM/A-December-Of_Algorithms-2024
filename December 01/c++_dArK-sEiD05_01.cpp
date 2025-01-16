#include <iostream>
#include <vector>
using namespace std;

int findMissingNumber(int N, vector<int> &array) {
    int totalSum = N * (N + 1) / 2;
    int arraySum = 0;
    for (int num : array) {
        arraySum += num;
    }
    return totalSum - arraySum;
}

int main() {
    int N = 5;
    vector<int> array = {1, 2, 4, 5};
    cout << findMissingNumber(N, array) << endl;
    return 0;
}
