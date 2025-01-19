//(29) The Maze of Weighted Portals:
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX 50
#define INF INT_MAX

typedef struct {
    int x, y;
} Point;

typedef struct {
    Point start, end;
    int weight;
} Portal;

typedef struct {
    int dist;
    Point pos;
} Node;

int N, M, P;
Portal portals[1000];
int grid[MAX][MAX];
int dist[MAX][MAX];
int visited[MAX][MAX];
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

int min(int a, int b) {
    return a < b ? a : b;
}

int isValid(int x, int y) {
    return x >= 0 && y >= 0 && x < N && y < M;
}

void dijkstra() {
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++) {
            dist[i][j] = INF;
            visited[i][j] = 0;
        }
    dist[0][0] = 0;
    Node pq[MAX * MAX];
    int size = 0;
    pq[size++] = (Node){0, {0, 0}};
    
    while (size > 0) {
        Node current = pq[--size];
        int x = current.pos.x, y = current.pos.y;
        if (visited[x][y]) continue;
        visited[x][y] = 1;
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (isValid(nx, ny) && dist[nx][ny] > dist[x][y]) {
                dist[nx][ny] = dist[x][y];
                pq[size++] = (Node){dist[nx][ny], {nx, ny}};
            }
        }
        
        for (int i = 0; i < P; i++) {
            if (portals[i].start.x == x && portals[i].start.y == y && dist[x][y] + portals[i].weight < dist[portals[i].end.x][portals[i].end.y]) {
                dist[portals[i].end.x][portals[i].end.y] = dist[x][y] + portals[i].weight;
                pq[size++] = (Node){dist[portals[i].end.x][portals[i].end.y], portals[i].end};
            }
        }
    }
}

int main() {
    scanf("%d %d", &N, &M);
    scanf("%d", &P);
    for (int i = 0; i < P; i++) {
        scanf("%d %d %d %d %d", &portals[i].start.x, &portals[i].start.y, &portals[i].end.x, &portals[i].end.y, &portals[i].weight);
        portals[i].start.x--;
        portals[i].start.y--;
        portals[i].end.x--;
        portals[i].end.y--;
    }
    
    dijkstra();
    printf("%d\n", dist[N-1][M-1]);
    return 0;
}

