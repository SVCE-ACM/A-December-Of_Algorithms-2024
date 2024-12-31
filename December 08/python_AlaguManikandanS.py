def digit_square_sum(n):
    return sum(int(digit) ** 2 for digit in str(n))

def total_digit_square_sum(N):
    total_sum = 0
    for num in range(1, N + 1):
        total_sum += digit_square_sum(num)
    return total_sum

N = int(input("Enter a positive integer N: "))
if N > 0:
    result = total_digit_square_sum(N)
    print(f"The total digit square sum from 1 to {N} is: {result}")
else:
    print("Please enter a positive integer.")
