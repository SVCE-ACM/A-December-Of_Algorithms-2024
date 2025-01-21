def minPlatforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    
    platforms_needed = 0
    max_platforms = 0
    i, j = 0, 0
    
    while i < len(arrivals) and j < len(departures):
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1
        
        max_platforms = max(max_platforms, platforms_needed)
    
    return max_platforms

arrivals = list(map(int, input("arrivals= ").split()))
departures = list(map(int, input("depatures= ").split()))
print(f"Minimum platforms required: {minPlatforms(arrivals, departures)}")
