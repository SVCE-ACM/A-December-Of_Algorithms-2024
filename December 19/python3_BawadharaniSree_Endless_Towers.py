def tower_of_hanoi(n, source, helper, destination, moves=None):
    if moves is None:
        moves = []
    
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {destination}")
        return moves
    
    tower_of_hanoi(n-1, source, destination, helper, moves)
    
    moves.append(f"Move disk {n} from {source} to {destination}")
    
    tower_of_hanoi(n-1, helper, source, destination, moves)
    
    return moves

def calculate_min_moves_and_sequence(n):
    moves = tower_of_hanoi(n, 'A', 'B', 'C')
    min_moves = len(moves)
    return min_moves, moves

n = int(input("Enter the number of golden disks: "))

min_moves, sequence = calculate_min_moves_and_sequence(n)

print(f"Minimum number of moves: {min_moves}")
print("Sequence of moves:")
for move in sequence:
    print(move)
