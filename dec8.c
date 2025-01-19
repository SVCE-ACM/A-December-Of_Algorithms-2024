//(8) digit manipulation:
#include<stdio.h>
int main(){
    int n,s=0;
    printf("enter number:");
    scanf("%d",&n);
    while(n!=0){
        if(n>=10){
            int m=n;
            while(m!=0){
                s=s+((m%10)*(m%10));
                m=m/10;
            }
            n=n-1;
        }
        else{
            s=s+(n*n);
            n=n-1;
        }
    }printf("square sum=%d",s);
    return 0;
}

