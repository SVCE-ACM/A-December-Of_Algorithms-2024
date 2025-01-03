def digit_square_sum(n):
    total_sum = 0
    for i in range(1, n + 1):
        digit_sum = sum(int(digit) ** 2 for digit in str(i))
        total_sum += digit_sum
    return total_sum

N = int(input("Enter a positive integer N: "))
result = digit_square_sum(N)
print("The total Digit Square Sum is:", result)