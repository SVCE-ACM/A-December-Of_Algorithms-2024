def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 0:
        return []

    moves = []
    moves.extend(tower_of_hanoi(n - 1, source, auxiliary, destination))
    moves.append((source, destination))
    moves.extend(tower_of_hanoi(n - 1, auxiliary, destination, source))

    return moves

if _name_ == "_main_":
    num_disks = 4
    start = "A"
    destination = "C"
    auxiliary = "B"
    moves = tower_of_hanoi(num_disks, start, destination, auxiliary)

    print(f"Minimum number of moves: {len(moves)}")
    print("Sequence of moves:")
    for i, move in enumerate(moves, 1):
        print(f"{i}. Move disk 1 from {move[0]} to {move[1]}")
