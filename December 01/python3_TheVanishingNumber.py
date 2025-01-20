# December 01 - The Vanishing Number


N = int(input("Enter the number of participants: "))

print("Enter the list in the following format, 1 2 3 4 5")
lst = list(map(int, input().split()))

# Missing number
mn = int(((N*(N+1))/2) - sum(lst))
print("The bib number of the missing participant is:", mn)


""" Solution from 1012 """