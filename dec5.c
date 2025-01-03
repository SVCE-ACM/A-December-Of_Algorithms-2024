//(5) Josephus Problem
#include<stdio.h>
int Josephus(int n,int k){
    if(n==1) return 0;
    else return(Josephus(n-1,k)+k)%n;
}
int main(){
    int n,k,arr[100],i;
    printf("enter number of people:");
    scanf("%d",&n);
    printf("enter person to be killed:");
    scanf("%d",&k);
    printf("%d",Josephus(n,k)+1);
    return 0;
}

