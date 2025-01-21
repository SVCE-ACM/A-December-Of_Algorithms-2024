#include <stdio.h>
#include <stdlib.h>

#define MAX_N 100005

int main() {
    int T;
    scanf("%d", &T);

    char result[T][4];
    
    int occurrences[MAX_N];
    
    for (int t = 0; t < T; t++) {
        int N, K, D;
        scanf("%d %d %d", &N, &K, &D);
        
        int A[N];
        
        for (int i = 0; i < MAX_N; i++) {
            occurrences[i] = 0;
        }
        
        for (int i = 0; i < N; i++) {
            scanf("%d", &A[i]);
        }
        
        for (int i = 0; i < N; i++) {
            occurrences[A[i]]++;
        }
        
        int possible = 0;
        for (int i = 1; i <= N; i++) {
            if (occurrences[i] >= D) {
                possible = 1;
                break;
            }
        }
        
        if (possible) {
            result[t][0] = 'Y';
            result[t][1] = 'E';
            result[t][2] = 'S';
            result[t][3] = '\0';
        } else {
            result[t][0] = 'N';
            result[t][1] = 'O';
            result[t][2] = '\0';
        }
    }

    for (int i = 0; i < T; i++) {
        printf("%s\n", result[i]);
    }

    return 0;
}
