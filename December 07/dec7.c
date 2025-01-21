#include<stdio.h>

int main()
{
    int n, i, j;
    printf("No. of floors: ");
    scanf("%d", &n);

    int l[n][n];

    for (i = 0; i < n; i++) {
        for (j = 0; j <= i; j++) {
            if (j == 0 || j == i) {
                l[i][j] = 1;
            } else {
                l[i][j] = l[i - 1][j - 1] + l[i - 1][j];
            }
        }
    }

    printf("[");
    for (i = 0; i < n; i++) {
        printf("[");
        for (j = 0; j <= i; j++) {
            printf("%d", l[i][j]);
        }
        printf("]");
        if (i < n - 1) {
            printf(", ");
        }
    }
    printf("]\n");

    return 0;
}
