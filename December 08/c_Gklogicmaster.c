#include <stdio.h>
int main() {
    int  n,sum=0;
    printf("enter a positive integer till which to find its digit square sum :");
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        int num =i;
        if(num<10){
            sum=sum+(num*num);
        }
        if(num>=10){
            int temp;
            while(num!=0){
            temp=num%10;
            sum=sum+(temp*temp);
            num=num/10;
            }
        }
    }
    printf("the total digit square sum of %d numbers is :%d",n,sum);
    return 0;
}
