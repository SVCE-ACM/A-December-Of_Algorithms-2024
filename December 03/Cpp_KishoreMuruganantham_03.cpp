#include <iostream>
#include <string>
#include <cmath>
using namespace std;

string alternatingSquareArrangement(int R, int B) {
    if (abs(R - B) > 1) {
        return "Not possible";
    }

    string result;
    int major, minor;
    char majorColor, minorColor;

    if (R >= B) {
        major = R;
        minor = B;
        majorColor = 'R';
        minorColor = 'B';
    } else {
        major = B;
        minor = R;
        majorColor = 'B';
        minorColor = 'R';
    }

    for (int i = 0; i < major + minor; i++) {
        if (major > 0) {
            result += majorColor;
            major--;
        }
        if (minor > 0 && (result.empty() || result.back() == majorColor)) {
            result += minorColor;
            minor--;
        }
    }

    return result;
}

int main() {
    // Test cases
    cout << alternatingSquareArrangement(3, 2) << endl; // Output: "RBRBR"
    cout << alternatingSquareArrangement(4, 2) << endl; // Output: "Not possible"
    return 0;
}
