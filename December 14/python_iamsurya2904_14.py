from collections import Counter

def can_split_squad(N, K, D, A):
  subject_counts = Counter(A)
  unique_subjects = len(subject_counts)

  if unique_subjects < K:
    return "NO"

  max_team_size = (N + D) // 2
  min_team_size = (N - D) // 2

  if sum(count for count in subject_counts.values() if count <= min_team_size) < K:
    return "NO"

  return "YES"
