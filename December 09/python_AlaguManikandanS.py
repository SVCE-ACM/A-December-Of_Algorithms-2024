def count_customers_with_one_return(returns):
    return returns.count(1)

returns1 = [2, 1, 5, 1, 0, 3, 1, 4, 1]
returns2 = [4, 3, 7, 2, 1, 0, 2, 1, 3]

print(f"Result for returns1: {count_customers_with_one_return(returns1)}")  
print(f"Result for returns2: {count_customers_with_one_return(returns2)}")  
