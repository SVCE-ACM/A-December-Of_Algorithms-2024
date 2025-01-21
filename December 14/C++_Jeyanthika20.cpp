#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

string canSplitSquad(int N, int K, int D, vector<int>& A) {
    unordered_map<int, int> subjectCounts;
    for (int subject : A) subjectCounts[subject]++;

    int uniqueSubjects = subjectCounts.size();
    if (uniqueSubjects < K) return "NO";

    int maxTeamSize = (N + D) / 2;
    int minTeamSize = (N - D) / 2;

    int count = 0;
    for (auto& entry : subjectCounts) {
        if (entry.second <= minTeamSize) count++;
    }

    return count < K ? "NO" : "YES";
}
