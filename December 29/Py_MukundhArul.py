import heapq

def minimum_weight_path(N, M, portals):
    graph = {(i, j): [] for i in range(1, N + 1) for j in range(1, M + 1)}

    for x1, y1, x2, y2, w in portals:
        graph[(x1, y1)].append(((x2, y2), w))
        graph[(x2, y2)].append(((x1, y1), w))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 1 <= ni <= N and 1 <= nj <= M:
                    graph[(i, j)].append(((ni, nj), 0))

    pq = [(0, (1, 1))]
    distances = {node: float('inf') for node in graph}
    distances[(1, 1)] = 0

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_node == (N, M):
            return current_dist

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return -1
