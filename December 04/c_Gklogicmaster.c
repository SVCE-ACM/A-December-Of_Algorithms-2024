#include <stdio.h>
int calculatePlants(int month) {
    if (month == 1 || month == 2) {
        return 1;
    }
    int p1 = 1, p2 = 1, current = 0;
    for (int i = 3; i <= month; i++) {
        current = p1 + p2;
        p2 = p1;
        p1 = current;
    }

    return current;
}

int main() {
    int month;
    printf("Enter the month number: ");
    scanf("%d", &month);
    if (month <= 0) {
        printf("Please enter a valid month number greater than 0.\n");
    } else {
        int plants = calculatePlants(month);
        printf("Number of plants in month %d: %d\n", month, plants);
    }

    return 0;
}
