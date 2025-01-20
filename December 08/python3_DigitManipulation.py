# December 08 - Digit Manipulation


# Return the digits of the num in a list
def return_digits(num):
    digits = []
    
    while (num > 0):
        digit = num % 10
        digits.append(digit)
        
        num = int(num/10)
        
    return digits

# Required function
def digit_square_sum(N):
    sum = 0
    
    for i in range(1, N+1):
        if (i<=9): sum += i**2
        else:
            for digit in return_digits(i):
                sum += digit**2
    return sum
    
    
num = int(input("Enter the number: "))
print("The Total Digit square sum is ",digit_square_sum(num))


""" Solution from 1012 """
    