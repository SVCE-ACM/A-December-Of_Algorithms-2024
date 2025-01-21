#include <iostream>
using namespace std;
int josephus(int n, int k) {
    if (n == 1)
        return 0; 
    return (josephus(n - 1, k) + k) % n;
}

int main() {
    int n, k;

    cout << "Enter the number of people (n): ";
    cin >> n;
    cout << "Enter the step count (k): ";
    cin >> k;
    int safe_position = josephus(n, k) + 1;

    cout << "The safe position is: " << safe_position << endl;

    return 0;
}
