def minTrips(houses, W):
    trips = 0
    currentLoad = 0

    for gifts in houses:
        if currentLoad + gifts <= W:
            currentLoad += gifts
        else:
            trips += 1
            currentLoad = gifts  
    if currentLoad > 0:
        trips += 1

    return trips

houses = [2, 3, 5, 2, 1]
W = 6
print(minTrips(houses, W)) 
