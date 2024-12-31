from itertools import permutations

def group_permutations(s):
    unique_permutations = set(''.join(p) for p in permutations(s))
    grouped = {}
    for perm in unique_permutations:
        first_letter = perm[0]
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append(perm)
    for key in grouped:
        grouped[key].sort()
    return grouped

s = input()
print(group_permutations(s))
