def tower_of_hanoi(n, start, helper, destination, moves):
    if n == 1:
        moves.append(f"Move disk 1 from {start} to {destination}")
        return
    tower_of_hanoi(n-1, start, destination, helper, moves)
    moves.append(f"Move disk {n} from {start} to {destination}")
    tower_of_hanoi(n-1, helper, start, destination, moves)

def main():
    n = int(input("Enter the number of disks: "))
    moves = []
    tower_of_hanoi(n, 'A', 'B', 'C', moves)
    
    print(f"Minimum number of moves: {2**n - 1}")
    print("Sequence of moves:")
    for i, move in enumerate(moves, start=1):
        print(f"{i}. {move}")

if __name__ == "__main__":
    main()
