from collections import deque

def max_affected_buildings(buildings):
    def is_within_radius(building1, building2):
        x1, y1, r1 = building1
        x2, y2, _ = building2
        return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2

    def bfs(start):
        visited = [False] * len(buildings)
        queue = deque([start])
        visited[start] = True
        count = 1

        while queue:
            current = queue.popleft()
            for neighbor in range(len(buildings)):
                if not visited[neighbor] and is_within_radius(buildings[current], buildings[neighbor]):
                    visited[neighbor] = True
                    queue.append(neighbor)
                    count += 1

        return count

    max_count = 0
    for i in range(len(buildings)):
        max_count = max(max_count, bfs(i))

    return max_count

# Get input from the user
n = int(input("Enter the number of buildings: "))
buildings = []
for _ in range(n):
    x, y, r = map(int, input("Enter x, y, and r (space-separated): ").split())
    buildings.append([x, y, r])

print(max_affected_buildings(buildings))
