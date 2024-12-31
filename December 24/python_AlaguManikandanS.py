from itertools import permutations

def group_permutations(s):
    unique_permutations = sorted(set(permutations(s)))
    grouped = {}
    for perm in unique_permutations:
        perm_str = ''.join(perm)
        first_letter = perm_str[0]
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append(perm_str)
    return grouped

s = "abc"
output = group_permutations(s)
print(output)
