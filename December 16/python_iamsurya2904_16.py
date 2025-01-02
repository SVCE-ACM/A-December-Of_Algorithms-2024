def min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    platforms_needed = 0
    current_platforms = 0

    i = 0
    j = 0

    while i < len(arrivals):
        if arrivals[i] <= departures[j]:
            current_platforms += 1
            i += 1
        else:
            current_platforms -= 1
            j += 1

        platforms_needed = max(platforms_needed, current_platforms)

    return platforms_needed
