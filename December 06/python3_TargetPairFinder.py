# December 06 - Target Pair Finder


# Inputs
print("Enter the list in the following format, 1 2 3 4 5\n")

# Removing duplicated elements (set)
# as well as maintaining the order (list)
lst = list(set(map(int, input().split())))

tsum = int(input("Enter the target sum: "))

# Unique pairs
up = []

for ele1 in lst:
    
    index = lst.index(ele1)
    
    for ele2 in lst[index:]:
        if ele1 + ele2 == tsum:
            pair = (ele1, ele2)
            if pair in up:
            	pass
            else:
            	up.append(pair)
  
            
print(up)


""" Solution from 1012 """