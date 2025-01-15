def HanoiTower(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    HanoiTower(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    HanoiTower(n - 1, auxiliary, target, source)

n = int(input("Enter number of disks: "))
print(f"Minimum No.Of Moves: {(2**n)-1}!\nThe Move Sequence:")
HanoiTower(n, 'A', 'C', 'B')

