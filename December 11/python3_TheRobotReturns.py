# December 11 - The Robot Returns


moves = list(input("Enter the moves sequence as a string: "))

pos = [0, 0]

for move in moves:
	
	# x-axis
	if move == 'R':
		pos[0]+=1
	elif move == 'L':
		pos[0]-=1 
	# y-axis	
	elif move == 'U':
		pos[1]+=1
	elif move == 'D':
		pos[1]-=1

print("true" if pos == [0, 0] else "false")


""" Solution from 1012 """