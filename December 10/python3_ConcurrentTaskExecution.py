# December 10 - Concurrent Task Execution


""" 
---------------- Important to note ----------------

-> I am not really sure how to get the task list from the console in a more efficient manner

-> So the following approach is taken to get the input

--> It is reccomended to just assign the list to the tasks variable in the source code itself!!
(line-17)

---------------------------------------------------------------
"""

tasks = []
# Order of execution
oe = [[]]

np = int(input("Enter the number of pairs: "))
print("Enter the pairs one by one in the following format, A B,C which is ('A', ['B', 'C'])\n")

for i in range(np):
	pair = input().split()
	ID = pair[0]
	dep = pair[1].split(",") if len(pair) == 2 else []
	tasks.append((ID, dep))


# Sorting based on the number of dependencies
tasks = sorted(tasks, key=lambda item: len(item[1]))


# Check if all the dependencies are present!
def is_there(depn):
	tot = len(depn)
	n = 0
	
	order = 0

	for t in depn:
		 for o in oe:
		 	if t in o:
		 		n+=1
		 		order = oe.index(o) if order < oe.index(o) else order
		
	# Checking if all the dependencies are there
	if n == tot:
		# Returning in which order the latest dependency runs + 1
		return (True, order+1)
	else:
		return (False, -1)


# Parsing
# To loop the tasks list
index = 0
# To ensure that we looped it only two times
count = 0

while(tasks and count < 2):

	if index == len(tasks):
				index = 0
				count += 1
	
	id = tasks[index][0]
	dpn = tasks[index][1]
	
	if dpn == []:
		oe[index].append(id)
		tasks.pop(0)
	else:
		value, order = is_there(dpn)
		if value:
			try:
				oe[order].append(id)
				tasks.pop(index)
			except:
				oe.append([])
				oe[order].append(id)
				tasks.pop(index)
		else:
			index += 1
				
if count == 2:
	print("Error: Cyclic dependency detected")
else:
	print(oe)
	

""" Solution from 1012 """