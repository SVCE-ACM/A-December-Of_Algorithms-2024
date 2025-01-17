#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

string canSplitSquad(int N, int K, int D, const vector<int> &A) {
    unordered_map<int, int> subject_counts;
    for (int subject : A) {
        subject_counts[subject]++;
    }

    int unique_subjects = subject_counts.size();
    if (unique_subjects < K) {
        return "NO";
    }

    int max_team_size = (N + D) / 2;
    int min_team_size = (N - D) / 2;

    int count_within_limit = 0;
    for (const auto &entry : subject_counts) {
        if (entry.second <= min_team_size) {
            count_within_limit++;
        }
    }

    if (count_within_limit < K) {
        return "NO";
    }

    return "YES";
}

int main() {
    int N = 10, K = 3, D = 2;
    vector<int> A = {1, 2, 2, 3, 3, 3, 4, 5, 5, 5};
    cout << canSplitSquad(N, K, D, A) << endl;
    return 0;
}
