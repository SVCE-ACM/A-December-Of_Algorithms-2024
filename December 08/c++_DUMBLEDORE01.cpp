#include <iostream>
using namespace std;

int digit_square_sum(int num) {
    int sum = 0;
    while (num > 0) {
        int digit = num % 10;
        sum += digit * digit;
        num /= 10;
    }
    return sum;
}

int calculate_total_digit_square_sum(int N) {
    int total_sum = 0;
    for (int num = 1; num <= N; ++num) {
        total_sum += digit_square_sum(num);
    }
    return total_sum;
}

int main() {
    int N;
    cout << "Enter a positive integer N: ";
    cin >> N;
    int total = calculate_total_digit_square_sum(N);
    cout << "Total Digit Square Sum from 1 to " << N << ": " << total << endl;
    return 0;
}
