#include <iostream>
#include <string>
using namespace std;

bool judgeCircle(string moves) {
    int x = 0, y = 0; 
    for (char move : moves) {
        if (move == 'R') x++;    
        else if (move == 'L') x--; 
        else if (move == 'U') y++; 
        else if (move == 'D') y--; 
    }

    return (x == 0 && y == 0);
}

int main() {
    string moves;
    cout << "Enter the moves: ";
    cin >> moves;

    if (judgeCircle(moves)) {
        cout << "The robot returns to the origin." << endl;
    } else {
        cout << "The robot does not return to the origin." << endl;
    }

    return 0;
}
