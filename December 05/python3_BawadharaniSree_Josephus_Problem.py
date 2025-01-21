def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1
n = int(input("Enter the number of people (n): "))
k = int(input("Enter the step size (k): "))
safe_position = josephus(n, k)
print(f"The safe position for n = {n} and k = {k} is: {safe_position}")