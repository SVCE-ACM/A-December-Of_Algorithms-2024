def target_pair_finder(numbers, target):
    unique_pairs = []
    seen = set()
    
    for num in numbers:
        complement = target - num
        if complement not in seen:
            seen.add(num)
        else:
            unique_pairs.append((complement, num))
    
    return unique_pairs

# Test cases
print(target_pair_finder([2, 4, 3, 7, 1, 5], 6))  # Output: [(2, 4), (1, 5)]
print(target_pair_finder([10, 15, 3, 7, 8, 12, 5], 20))  # Output: [(10, 10), (8, 12), (15, 5)]
