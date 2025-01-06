def tower_of_hanoi(n, source, helper, destination, moves=None):
    if moves is None:
        moves = []
    
    # Base case: only one disk, move it directly from source to destination
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {destination}")
        return moves
    
    # Move n-1 disks from source to helper
    tower_of_hanoi(n-1, source, destination, helper, moves)
    
    # Move the nth disk from source to destination
    moves.append(f"Move disk {n} from {source} to {destination}")
    
    # Move the n-1 disks from helper to destination
    tower_of_hanoi(n-1, helper, source, destination, moves)
    
    return moves

def calculate_min_moves_and_sequence(n):
    moves = tower_of_hanoi(n, 'A', 'B', 'C')
    min_moves = len(moves)
    return min_moves, moves

# Input from the user
n = int(input("Enter the number of golden disks: "))

# Calculate and display the result
min_moves, sequence = calculate_min_moves_and_sequence(n)

print(f"Minimum number of moves: {min_moves}")
print("Sequence of moves:")
for move in sequence:
    print(move)
