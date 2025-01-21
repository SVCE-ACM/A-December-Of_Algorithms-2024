from itertools import permutations

def group_permutations(s):
    # Generate all unique permutations of the string
    unique_perms = sorted(set(''.join(p) for p in permutations(s)))

    # Group permutations by their first letter
    grouped = {}
    for perm in unique_perms:
        first_letter = perm[0]
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append(perm)

    return grouped

# Input string from the user
s = input("Enter a string: ")
result = group_permutations(s)

# Print the grouped permutations
for key in sorted(result):
    print(f"'{key}': {result[key]}")
