def safe_position(n, k):
    if n == 1:
        return 1
    else:
        return (safe_position(n - 1, k) + k - 1) % n + 1

n1, k1 = 3, 2
n2, k2 = 5, 3
print(safe_position(n1, k1))  
print(safe_position(n2, k2))  
