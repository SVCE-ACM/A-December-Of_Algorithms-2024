#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<pair<string, string>> tower_of_hanoi(int n, string source, string destination, string auxiliary) {
    vector<pair<string, string>> moves;
    
    if (n == 0) {
        return moves;
    }

    vector<pair<string, string>> first_half = tower_of_hanoi(n - 1, source, auxiliary, destination);
    moves.insert(moves.end(), first_half.begin(), first_half.end());
    
    moves.push_back({source, destination});
    
    vector<pair<string, string>> second_half = tower_of_hanoi(n - 1, auxiliary, destination, source);
    moves.insert(moves.end(), second_half.begin(), second_half.end());
    
    return moves;
}

int main() {
    int num_disks = 4;
    string start = "A";
    string destination = "C";
    string auxiliary = "B";

    vector<pair<string, string>> moves = tower_of_hanoi(num_disks, start, destination, auxiliary);

    cout << "Minimum number of moves: " << moves.size() << endl;
    cout << "Sequence of moves:" << endl;
    for (int i = 0; i < moves.size(); i++) {
        cout << i + 1 << ". Move disk from " << moves[i].first << " to " << moves[i].second << endl;
    }

    return 0;
}
