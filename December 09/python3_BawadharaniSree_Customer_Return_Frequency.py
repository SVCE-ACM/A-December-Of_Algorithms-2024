def count_customers(returns):
    return returns.count(1)

returns = list(map(int, input("Enter the return frequencies separated by spaces: ").split()))
result = count_customers(returns)
print(result)