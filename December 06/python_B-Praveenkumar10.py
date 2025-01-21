def find_pairs(numbers, target):
    unique_pairs = []
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):  
            if numbers[i] + numbers[j] == target:
                pair = (numbers[i], numbers[j])
                if pair not in unique_pairs:
                    unique_pairs.append(pair)
    
    return unique_pairs

numbers1 = [2, 4, 3, 7, 1, 5]
target1 = 6
print("Unique pairs:", find_pairs(numbers1, target1))

numbers2 = [10, 15, 3, 7, 8, 12, 5]
target2 = 20
print("Unique pairs:", find_pairs(numbers2, target2))
