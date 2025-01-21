def find_target_pairs(numbers, target):
    unique_pairs = []
    visited = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pair = tuple(sorted((numbers[i], numbers[j])))
                if pair not in visited:
                    unique_pairs.append(pair)
                    visited.add(pair)
    return unique_pairs

numbers_input = input("Enter a list of integers (comma-separated): ")
numbers = list(map(int, numbers_input.split(',')))
target = int(input("Enter the target sum: "))
result = find_target_pairs(numbers, target)
print("Unique pairs are:", result)