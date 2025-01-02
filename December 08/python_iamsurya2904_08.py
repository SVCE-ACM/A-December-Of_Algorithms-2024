def digit_square_sum(N):
    def digit_square_sum_of_number(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

    total_sum = 0
    for i in range(1, N + 1):
        total_sum += digit_square_sum_of_number(i)
    return total_sum
