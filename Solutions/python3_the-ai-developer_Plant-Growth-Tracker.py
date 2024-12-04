import math
N = int(input("Enter No.Of Months: "))
print(f"No.Of Plants(Predicted!): {int(((1+math.sqrt(5))**N-(1-math.sqrt(5))**N)//(2**N*math.sqrt(5)))}")
