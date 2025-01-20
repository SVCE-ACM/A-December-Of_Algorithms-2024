# December 05 - Josephus Problem


N = int(input("Enter the number of persons: "))

# No of persons to be moved
nfpm = int(input("Enter the number of persons to be counted: ")) - 1

# Creating the list of the persons
lst = list(range(1, N+1))

# The first person to be killed
index = nfpm
lst.pop(index)

while True:
    
    # Making the list as the circle
    for i in range(nfpm):
    	index += 1
    	if index == len(lst):
    		index= 0
    
    lst.pop(index)
    
    # If the index was refered the last element
    index = 0 if index == len(lst) else index
    	
    if len(lst) == 1:
        break

print(lst[0])


""" Solution from 1012 """