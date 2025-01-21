from collections import Counter

def solve():
    t = int(input("Enter number of test cases: "))
    print(f"You entered number of test cases: {t}")  
    results = []
    
    for i in range(t):
        print(f"\nTest case {i + 1}:")
        n, k, d = map(int, input("Enter N, K, D: ").split())
        print(f"You entered N = {n}, K = {k}, D = {d}")  
        
        subjects = list(map(int, input("Enter subjects: ").split()))
        print(f"You entered subjects: {subjects}")  
        
        freq = Counter(subjects)
        distinct_subjects = len(freq)
        
        if distinct_subjects < 2 * k:
            results.append("NO")
            continue
        
        subject_counts = list(freq.values())
        subject_counts.sort(reverse=True)
        
        team1_size, team2_size = 0, 0
        unique_team1, unique_team2 = 0, 0
        
        for count in subject_counts:
            if unique_team1 < k:
                team1_size += count
                unique_team1 += 1
            elif unique_team2 < k:
                team2_size += count
                unique_team2 += 1
            
            if unique_team1 == k and unique_team2 == k and abs(team1_size - team2_size) <= d:
                results.append("YES")
                break
        else:
            results.append("NO")
    
    print("\nResults:")
    print("\n".join(results))

solve()
