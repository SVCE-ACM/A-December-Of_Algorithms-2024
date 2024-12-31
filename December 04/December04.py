def main():
    n = int(input('Enter the months : '))
    f0=0
    f1=1
    fib=0
    if(n==1):
        print(1)
        return
    for i in range(1,n):
        fib=f0+f1
        f0=f1
        f1=fib
    print(fib)
if __name__=="__main__":
    main()