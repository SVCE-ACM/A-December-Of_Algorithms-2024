import heapq

def min_weight_path(N, M, P, portals):
    dist = [[float('inf')] * M for _ in range(N)]
    dist[0][0] = 0
    
    pq = [(0, 0, 0)]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    portals = [(x1-1, y1-1, x2-1, y2-1, w) for x1, y1, x2, y2, w in portals]

    portal_graph = {}
    for (x1, y1, x2, y2, w) in portals:
        if (x1, y1) not in portal_graph:
            portal_graph[(x1, y1)] = []
        if (x2, y2) not in portal_graph:
            portal_graph[(x2, y2)] = []
        portal_graph[(x1, y1)].append((x2, y2, w))
        portal_graph[(x2, y2)].append((x1, y1, w))

    while pq:
        weight, x, y = heapq.heappop(pq)

        if x == N - 1 and y == M - 1:
            return weight
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                new_weight = weight
                if new_weight < dist[nx][ny]:
                    dist[nx][ny] = new_weight
                    heapq.heappush(pq, (new_weight, nx, ny))
        
        if (x, y) in portal_graph:
            for (nx, ny, w) in portal_graph[(x, y)]:
                new_weight = weight + w
                if new_weight < dist[nx][ny]:
                    dist[nx][ny] = new_weight
                    heapq.heappush(pq, (new_weight, nx, ny))

    return dist[N-1][M-1] if dist[N-1][M-1] != float('inf') else -1

N, M = map(int, input("Enter the grid dimensions (N M): ").split())
P = int(input("Enter the number of portals: "))
portals = []
for _ in range(P):
    x1, y1, x2, y2, w = map(int, input("Enter portal details (x1 y1 x2 y2 weight): ").split())
    portals.append((x1, y1, x2, y2, w))

result = min_weight_path(N, M, P, portals)
print(result)
