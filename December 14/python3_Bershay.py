def can_divide_students(t, test_cases):
    results = []
    for case in test_cases:
        n, k, d, subjects = case
        unique_subjects = len(set(subjects))
        if k > unique_subjects or unique_subjects > 2 * k or n < 2:
            results.append("NO")
            continue

        min_team_size = max(1, n // 2 - d // 2)
        max_team_size = min(n // 2 + d // 2, n - min_team_size)

        team1 = set()
        team2 = set()

        for subject in subjects:
            if len(team1) < max_team_size and (len(team1) < k or subject in team1):
                team1.add(subject)
            elif len(team2) < max_team_size and (len(team2) < k or subject in team2):
                team2.add(subject)

        if len(team1) >= min_team_size and len(team2) >= min_team_size and len(team1) <= max_team_size and len(team2) <= max_team_size:
            results.append("YES")
        else:
            results.append("NO")

    return results

t = int(input())
test_cases = []
for _ in range(t):
    n, k, d = map(int, input().split())
    subjects = list(map(int, input().split()))
    test_cases.append((n, k, d, subjects))

results = can_divide_students(t, test_cases)
for result in results:
    print(result)
