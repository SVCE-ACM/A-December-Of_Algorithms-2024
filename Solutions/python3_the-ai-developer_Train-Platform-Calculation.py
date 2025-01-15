def CalcMinReqPlatforms(arr, dept):

    """ arr.sort()
    dept.sort()"""
    i = j = 0
    platforms = 0
    max_platforms = 0

    while i < len(arr) and j < len(dept):
        if arr[i] <= dept[j]:
            platforms += 1
            i += 1
            max_platforms = max(max_platforms, platforms)
        else:
            platforms -= 1
            j += 1

    return max_platforms

print(f"Minimum Platforms Required: {CalcMinReqPlatforms(list(map(int,input('Enter Arrival Timings: ').split())),list(map(int,input('Enter Departure Timings: ').split())))}")
