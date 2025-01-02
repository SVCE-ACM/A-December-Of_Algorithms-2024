def josephus(n, k):
    safe_position = 0
    for i in range(1, n + 1):
        safe_position = (safe_position + k) % i
    return safe_position + 1

# Test cases
print(josephus(3, 2))  # Output: 3
print(josephus(5, 3))  # Output: 4
