//(22) Earthquake Propagation
#include <stdio.h>
#include <math.h>

typedef struct {
    int x, y, r;
} Building;

int distance(Building a, Building b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

int affected_buildings(Building buildings[], int n, int start) {
    int count = 0;
    int visited[n];
    for (int i = 0; i < n; i++) visited[i] = 0;
    
    visited[start] = 1;
    count++;
    for (int i = 0; i < n; i++) {
        if (!visited[i] && distance(buildings[start], buildings[i]) <= buildings[start].r) {
            visited[i] = 1;
            count++;
        }
    }
    return count;
}

int max_affected(Building buildings[], int n) {
    int max_count = 0;
    for (int i = 0; i < n; i++) {
        int affected = affected_buildings(buildings, n, i);
        if (affected > max_count) max_count = affected;
    }
    return max_count;
}

int main() {
    int n;
    scanf("%d", &n);
    
    Building buildings[n];
    for (int i = 0; i < n; i++) {
        scanf("%d %d %d", &buildings[i].x, &buildings[i].y, &buildings[i].r);
    }
    
    printf("%d\n", max_affected(buildings, n));
    return 0;
}

