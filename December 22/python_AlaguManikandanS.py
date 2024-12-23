import math

def can_affect(building1, building2):
    x1, y1, r1 = building1
    x2, y2, r2 = building2
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance <= r1 + r2

def dfs(building, buildings, affected):
    affected.add(building)
    for i, b in enumerate(buildings):
        if i not in affected and can_affect(buildings[building], b):
            dfs(i, buildings, affected)

def max_affected_buildings(buildings):
    n = len(buildings)
    max_affected = 0
    for i in range(n):
        affected = set()
        dfs(i, buildings, affected)
        max_affected = max(max_affected, len(affected))
    return max_affected

print(max_affected_buildings([[2,1,3],[6,1,4]]))
print(max_affected_buildings([[1,1,5],[10,10,5]]))
