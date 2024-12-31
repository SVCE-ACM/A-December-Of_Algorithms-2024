def min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    
    n = len(arrivals)
    platforms_needed = 0
    max_platforms = 0
    
    i = 0 
    j = 0  
    
    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:
            platforms_needed -= 1
            j += 1
    
    return max_platforms

arrivals = list(map(int, input().split()))
departures = list(map(int, input().split()))

result = min_platforms(arrivals, departures)
print(f"Minimum platforms required: {result}")
