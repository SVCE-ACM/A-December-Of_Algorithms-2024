def find_unique_pairs(numbers, target):
    unique_pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):  
            if numbers[i] + numbers[j] == target:
                unique_pairs.append((numbers[i], numbers[j]))

    return unique_pairs

def get_input():
    numbers = input("Enter a list of integers separated by spaces: ")
    numbers = [int(num) for num in numbers.split()]
    target = int(input("Enter the target sum: "))
    return numbers, target
if _name_ == "_main_":
    numbers, target = get_input()
    result = find_unique_pairs(numbers, target)
    if result:
        print("Unique pairs are:", result)
    else:
        print("No unique pairs found that sum to", target)
