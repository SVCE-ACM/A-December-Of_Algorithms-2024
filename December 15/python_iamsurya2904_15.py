def min_trips(houses, W):
    trips = 0
    current_load = 0

    for gifts in houses:
        if current_load + gifts > W:
            trips += 1
            current_load = 0
        current_load += gifts

    if current_load > 0:
        trips += 1

    return trips
