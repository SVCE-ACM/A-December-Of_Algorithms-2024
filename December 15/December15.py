#minTrips(houses, W)
houses = list(map(int, input().split()))
W = int(input())
trips = 0
temp = 0
for i in houses:
    if temp + i > W:
        trips += 1
        temp = 0
    temp += i

if temp > 0:
    trips += 1

print(trips)
