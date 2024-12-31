//(4) Plant Growth Tracker-fibonacci series
#include<stdio.h>
int main(){
    int n,i,f=1,s=1,t;
    printf("enter number of month:");
    scanf("%d",&n);
    for(i=0;i<n-2;i++){
        t=f+s;
        f=s;
        s=t;
    }printf("in %d month number of plants is %d",n,t);
    return 0;
}
