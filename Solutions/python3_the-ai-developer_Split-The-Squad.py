from collections import Counter

def SplitTheSquad():
    T = int(input("Enter No.Of Entities: "))
    results = []

    for x in range(T):
        N, K, D = map(int, input(f"Enter The Values Of N,K And D Of Entity {x+1}: ").split())
        A = list(map(int, input(f"Enter The List(A) Of Entitity {x+1}: ").split()))
        freq = Counter(A)
        U_total = len(freq)

        if U_total < 2 * K:
            results.append("NO")
            continue

        counts = sorted(freq.values(), reverse=True)
        team1_count, team2_count = 0, 0
        team1_uniques, team2_uniques = 0, 0

        for count in counts:
            if team1_uniques < K:
                team1_count += count
                team1_uniques += 1
            elif team2_uniques < K:
                team2_count += count
                team2_uniques += 1
            else:
                break

        if team1_uniques == K and team2_uniques == K and abs(team1_count - team2_count) <= D:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

SplitTheSquad()

