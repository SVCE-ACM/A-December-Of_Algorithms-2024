def Josephus(List,CrntIdx,k):
    if len(List)==1:
        return List[0]
    CrntIdx=(CrntIdx+k)%len(List)
    del List[CrntIdx]
    return Josephus(List,CrntIdx,k)

NPpl,k=list(map(int,input("Enter No.Of Peoples And The Kill Count: ").split()))
print(f"In Order To Be In A Safe Zone, You Need To Stand At: {Josephus([x for x in range(1,NPpl+1)],0,k-1)}")
