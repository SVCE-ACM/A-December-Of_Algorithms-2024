def tower_of_hanoi(n, source, helper, destination, moves):
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, destination, helper, moves)
    moves.append(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, helper, source, destination, moves)

num_disks = 4
moves_list = []
tower_of_hanoi(num_disks, "A", "B", "C", moves_list)

print(f"Minimum number of moves: {len(moves_list)}")
print("Sequence of moves:")
for i, move in enumerate(moves_list, 1):
    print(f"{i}. {move}")
