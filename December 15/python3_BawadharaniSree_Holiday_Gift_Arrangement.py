def minTrips(houses, W):
    trip_count = 0
    current_sum = 0
    
    for gifts in houses:
        if current_sum + gifts > W:
            trip_count += 1
            current_sum = gifts
        else:
            current_sum += gifts
    
    if current_sum > 0:
        trip_count += 1
    
    return trip_count

houses = list(map(int, input("Houses= ").split()))
W = int(input("W="))
print(minTrips(houses, W))
