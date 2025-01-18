#include <stdio.h>
int position(int n, int k) {
    int result = 0;
    for (int i = 2; i <= n; i++) {
        result = (result + k) % i;
    }
    return result + 1;
}

int main() {
    int n, k;
    printf("Enter the number of people in the circle: ");
    scanf("%d", &n);

    printf("Enter the step count (k): ");
    scanf("%d", &k);
    if (n <= 0 || k <= 0) {
        printf("Invalid input. Both n and k must be greater than 0.\n");
        return 1;
    }
    int survivor = position(n, k);
    printf("The last person remaining is at position: %d\n", survivor);

    return 0;
}
