# December 15 - Holiday Gift Arrangement


houses = list(map(int, input("Enter the array in a space-separated format: \n").split()))

print("The W should be greater or equal than {} to run this algorithm".format(max(houses)) )
W = int(input("Enter the maximum carrying value of Santa’s sleigh: "))

def minTrips(houses, W):
	
	# Condition of W
	if W < max(houses):
		print("The W doesn't satisfy the condition ")
		return -1
	
	groups = [[0]]
	
	# group number
	gn = 0
	
	while(houses):
	
		if sum(groups[gn]) + houses[0] <= W:
			groups[gn].append(houses[0])
			houses.pop(0)
	
		else:
			groups.append([0])
			gn+=1
	
	return len(groups)

# Test
print(minTrips(houses, W))
	
""" Solution from 1012 """