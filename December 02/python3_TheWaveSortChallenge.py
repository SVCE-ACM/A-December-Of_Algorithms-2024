# December 02 - The Wave Sort Challenge


print("Enter the list of integers in the folllowing format, 1 2 3 4 5")
lst= list(map(int, input().split()))

# Sorting the list in ascending order
lst.sort()

# Wave Array
wa = []

while(len(lst)>1):
	wa.append(lst.pop(-1))
	wa.append(lst.pop(0))

# Appending the last element in the list
if lst:
	wa.append(lst[0])

print(wa)


""" Solution from 1012 """