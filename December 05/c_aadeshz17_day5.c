#include<stdio.h>
int josephus(int n,int k){
    if (n == 1) 
        return 0;
    else 
        return (josephus(n-1,k)+ k)%n;
}
void main()
{
int n,k,safeplayer;
printf("Enter No of People: ");
scanf("%d",&n);
printf("Enter Count: ");
scanf("%d",&k);
safeplayer=josephus(n,k)+1;
printf("Safeplayer: %d",safeplayer);
}