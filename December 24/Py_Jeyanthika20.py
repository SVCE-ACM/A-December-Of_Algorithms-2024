from itertools import permutations
from collections import defaultdict

def group_permutations(s):
    unique_permutations = sorted(set(permutations(s)))
    grouped = defaultdict(list)
    for perm in unique_permutations:
        grouped[perm[0]].append(''.join(perm))
    return dict(grouped)

input_string = "abc"
result = group_permutations(input_string)
print(result)
