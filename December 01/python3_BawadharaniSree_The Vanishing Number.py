N=int(input("Enter the Number of participants: "))
arr=list(map(int,input("Enter bib number with sapce:").split()))
total_sum=(N*(N+1))//2
missing_bib=total_sum-sum(arr)
print("The missing BIB: ",missing_bib)