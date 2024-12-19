def find_min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()

    i, j = 0, 0
    n = len(arrivals)

    platforms_needed = 0
    max_platforms = 0

    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1

        max_platforms = max(max_platforms, platforms_needed)

    return max_platforms

arrivals1 = [900, 940, 950, 1100, 1500, 1800]
departures1 = [910, 1200, 1120, 1130, 1900, 2000]
arrivals2 = [1030, 1015, 1045, 1100, 1500, 1530]
departures2 = [1040, 1105, 1050, 1130, 1515, 1600]

print("Minimum platforms required:", find_min_platforms(arrivals1, departures1))
print("Minimum platforms required:", find_min_platforms(arrivals2, departures2))
