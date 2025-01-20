# December 07 - The Magical Tower


# No of rows
N = int(input("Enter the number of rows: "))

# The list that will contain all the floors
lst = []

for floor in range(1, N+1):
	
	# Temporary list
	tlst = []
	
	# Making every elements of the floor to one
	for i in range(0, floor):
		tlst.append(1)
	
	# Replacing Non-one elements in the respective floors' indices
	if floor >= 3:
		for i in range(1, floor-1):
			tlst[i] = lst[-1][i] + lst[-1][i-1]
	
	lst.append(tlst)

print(lst[0] if N == 1 else lst)


""" Solution from 1012 """