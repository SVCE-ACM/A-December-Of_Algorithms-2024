moves = input("Enter Path: ")
print(f"{True if (moves.count('U') - moves.count('D') == 0 and moves.count('L') - moves.count('R') == 0) else False}")
