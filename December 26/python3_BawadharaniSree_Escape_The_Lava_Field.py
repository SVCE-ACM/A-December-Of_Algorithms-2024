def can_escape_lava_field(nums):
    max_reachable = 0
    for i, jump in enumerate(nums):
        if i > max_reachable:
            return False  # If the current position is beyond the farthest reachable index
        max_reachable = max(max_reachable, i + jump)
    return max_reachable >= len(nums) - 1

# Get input from the user
def main():
    print("Escape the Lava Field")
    nums = list(map(int, input("Enter the array of numbers separated by spaces: ").split()))
    if can_escape_lava_field(nums):
        print("Output: True (You can escape the lava field!)")
    else:
        print("Output: False (You cannot escape the lava field!)")

if __name__ == "__main__":
    main()
