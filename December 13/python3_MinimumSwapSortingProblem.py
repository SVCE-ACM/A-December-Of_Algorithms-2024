# December 13 - Minimum Swap Sorting Problem


N = int(input("Enter the number of integers: "))
lst = list(map(int, input("Enter the space-separated values: \n").split())) 

cost = 0

for i in range(0, len(lst)-1):
	
	# Minimum value
	mv = min(lst[i:])
	mv_i = lst.index(mv, i)
	
	# Swapping
	if lst[i] > mv:
		lst[i], lst[mv_i] = lst[mv_i], lst[i]
		cost += 1

print(cost)


""" Solution from 1012 """