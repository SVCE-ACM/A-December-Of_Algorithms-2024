//(14) split the sq:
#include <stdio.h>
#include <stdlib.h>

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int N, K, D;
        scanf("%d %d %d", &N, &K, &D);
        int A[N], freq[N+1];
        for (int i = 0; i <= N; i++) freq[i] = 0;
        for (int i = 0; i < N; i++) {
            scanf("%d", &A[i]);
            freq[A[i]]++;
        }
        
        int unique = 0;
        for (int i = 1; i <= N; i++) {
            if (freq[i] > 0) unique++;
        }
        
        if (unique < K) {
            printf("NO\n");
        } else {
            int team_size1 = N / 2;
            int team_size2 = N - team_size1;
            if (team_size1 <= team_size2 + D && team_size2 <= team_size1 + D) {
                printf("YES\n");
            } else {
                printf("NO\n");
            }
        }
    }
    return 0;
}

