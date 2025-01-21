import heapq
from collections import defaultdict

def minimum_weight_to_reach_target(N, M, P, portals):
    graph = defaultdict(list)
    for x1, y1, x2, y2, W in portals:
        graph[(x1, y1)].append(((x2, y2), W))
        graph[(x2, y2)].append(((x1, y1), W))

    pq = [(0, 1, 1)]
    visited = set()

    while pq:
        cost, x, y = heapq.heappop(pq)

        if (x, y) == (N, M):
            return cost

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= N and 1 <= ny <= M and (nx, ny) not in visited:
                heapq.heappush(pq, (cost, nx, ny))

        for (nx, ny), w in graph[(x, y)]:
            if (nx, ny) not in visited:
                heapq.heappush(pq, (cost + w, nx, ny))

    return -1

N = 4
M = 4
P = 3
portals = [
    (1, 1, 2, 3, 5),
    (2, 3, 4, 4, 2),
    (1, 2, 4, 1, 8),
]

print(minimum_weight_to_reach_target(N, M, P, portals))
