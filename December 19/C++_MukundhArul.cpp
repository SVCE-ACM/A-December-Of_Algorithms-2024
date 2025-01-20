#include <iostream>
#include <vector>
using namespace std;

void towerOfHanoi(int n, char source, char destination, char auxiliary, vector<pair<char, char>>& moves) {
    if (n == 0) return;

    towerOfHanoi(n - 1, source, auxiliary, destination, moves);
    moves.emplace_back(source, destination);
    towerOfHanoi(n - 1, auxiliary, destination, source, moves);
}

int main() {
    int numDisks = 4;
    vector<pair<char, char>> moves;

    towerOfHanoi(numDisks, 'A', 'C', 'B', moves);

    cout << "Minimum number of moves: " << moves.size() << endl;
    for (size_t i = 0; i < moves.size(); i++) {
        cout << i + 1 << ". Move disk from " << moves[i].first << " to " << moves[i].second << endl;
    }

    return 0;
}
