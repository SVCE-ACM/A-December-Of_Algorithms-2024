def DigitSqrSum(n):
    def DigitSum(x):
        square_sum=0
        while x>0:
            digit=x%10
            square_sum+=digit*digit
            x//=10
        return square_sum
    total_sum=0
    for i in range(1,n+1):
        total_sum += DigitSum(i)    
    return total_sum

print(f"Resultant Sum: {DigitSqrSum(int(input('Enter A Number: ')))}")

