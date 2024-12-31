import math

def maxAffectedBuildings(buildings):
    def isAffected(building1, building2):
        x1, y1, r1 = building1
        x2, y2, r2 = building2
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return distance <= r1 or distance <= r2
    
    def dfs(building, affected, visited):
        visited[building] = True
        affected_count = 1
        for i in range(len(buildings)):
            if not visited[i] and isAffected(buildings[building], buildings[i]):
                affected_count += dfs(i, affected, visited)
        return affected_count
    
    max_affected = 0
    for i in range(len(buildings)):
        visited = [False] * len(buildings)
        affected = dfs(i, [], visited)
        max_affected = max(max_affected, affected)
    
    return max_affected


n = int(input("Enter the number of buildings: "))
buildings = []

for _ in range(n):
    x, y, r = map(int, input().split())
    buildings.append([x, y, r])
print(maxAffectedBuildings(buildings))
