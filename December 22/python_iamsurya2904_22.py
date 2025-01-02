from math import sqrt

def earthquake_propagation(buildings):
    max_affected = 0

    for i in range(len(buildings)):
        affected = 1
        for j in range(len(buildings)):
            if i != j:
                distance = sqrt(
                    (buildings[i][0] - buildings[j][0])*2 + (buildings[i][1] - buildings[j][1])*2
                )
                if distance <= buildings[i][2]:
                    affected += 1
        max_affected = max(max_affected, affected)

    return max_affected

buildings = [[2, 1, 3], [6, 1, 4]]
max_affected = earthquake_propagation(buildings)
print(max_affected)  
