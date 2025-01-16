#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>

using namespace std;

vector<vector<string>> findTaskOrder(const vector<pair<string, vector<string>>> &tasks) {
    unordered_map<string, vector<string>> graph;
    unordered_map<string, int> in_degree;
    unordered_set<string> all_tasks;

    for (const auto &task : tasks) {
        string current = task.first;
        all_tasks.insert(current);

        for (const string &dependency : task.second) {
            graph[dependency].push_back(current);
            in_degree[current]++;
            all_tasks.insert(dependency);
        }
    }

    queue<string> q;
    for (const string &task : all_tasks) {
        if (in_degree[task] == 0) {
            q.push(task);
        }
    }

    vector<vector<string>> result;

    while (!q.empty()) {
        vector<string> concurrent_tasks;
        int size = q.size();

        for (int i = 0; i < size; ++i) {
            string task = q.front();
            q.pop();
            concurrent_tasks.push_back(task);

            for (const string &neighbor : graph[task]) {
                in_degree[neighbor]--;
                if (in_degree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }

        result.push_back(concurrent_tasks);
    }

    for (const auto &entry : in_degree) {
        if (entry.second > 0) {
            throw runtime_error("Error: Cyclic dependency detected");
        }
    }

    return result;
}

int main() {
    vector<pair<string, vector<string>>> tasks = {
        {"TaskA", {}},
        {"TaskB", {"TaskA"}},
        {"TaskC", {"TaskB"}},
        {"TaskD", {"TaskB", "TaskC"}}
    };

    try {
        vector<vector<string>> order = findTaskOrder(tasks);
        for (const auto &level : order) {
            for (const string &task : level) {
                cout << task << " ";
            }
            cout << endl;
        }
    } catch (const runtime_error &e) {
        cout << e.what() << endl;
    }

    return 0;
}
