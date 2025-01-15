def minTrips(houses, W):
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

print(f"Required Minimum No.Of Trips: {minTrips(list(map(int, input('Enter Gifts For Houses: ').split())), int(input('Enter Max Capacity: ')))}")

