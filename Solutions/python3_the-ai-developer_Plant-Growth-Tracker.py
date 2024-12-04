NMonth=int(input("Enter No.Of Months: "))
def NthFibo(N):
    if N<=1 and not N<0:
        return N
    return NthFibo(N-1)+NthFibo(N-2)

print(f"No.Of Plants(Predicted!): {NthFibo(NMonth)}")
