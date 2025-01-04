def robot_returns_to_origin(moves):
    x, y = 0, 0
    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'R':
            x += 1
        elif move == 'L':
            x -= 1
    return x == 0 and y == 0

if __name__ == "__main__":
    moves = input("Enter the robot's moves: ")
    print("Output:", robot_returns_to_origin(moves))