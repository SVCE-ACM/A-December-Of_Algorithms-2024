# December 03 - Alternating Square Arrangement


R = int(input("Enter the number of red squares: "))
B = int(input("Enter the number of blue squares: "))

more = max(R, B)
less = min(R, B)

if more-1 == less or more == less:
	if more == R:
		print("RB"*less, "" if more==less else "R", sep="")
	else:
		print("BR"*less, "" if more==less else "B", sep="")
else:
	print("Not Possible")
	
	
""" Solution from 1012 """