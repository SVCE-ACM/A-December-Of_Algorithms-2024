s = str(input("Enter string:"))
flag=0
flag1=0
if s.count("U")==s.count("D"):
    flag=1
if s.count("L")==s.count("R"):
    flag1=1
if flag==1 and flag1==1:
    print("True")
else:
    print("False")
