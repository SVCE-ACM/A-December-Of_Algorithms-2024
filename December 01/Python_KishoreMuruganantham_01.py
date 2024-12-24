def find_missing_number(N, array):
    expected_sum = N * (N + 1) // 2
    actual_sum = sum(array)
    return expected_sum - actual_sum

# Test cases
print(find_missing_number(5, [1, 2, 4, 5]))  # Output: 3
print(find_missing_number(3, [1, 3]))        # Output: 2
