//(19) Endless Towers
#include <stdio.h>

void move_disk(int n, char start, char end) {
    printf("Move disk %d from %c to %c\n", n, start, end);
}

void tower_of_hanoi(int n, char start, char helper, char end) {
    if (n == 1) {
        move_disk(1, start, end);
        return;
    }
    tower_of_hanoi(n - 1, start, end, helper);
    move_disk(n, start, end);
    tower_of_hanoi(n - 1, helper, start, end);
}

int main() {
    int n = 4;
    printf("Minimum number of moves: %d\n", (1 << n) - 1);
    tower_of_hanoi(n, 'A', 'B', 'C');
    return 0;
}

