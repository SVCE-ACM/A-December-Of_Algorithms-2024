#include<stdio.h>
void main()
{
int cusret[100],n,returns=0,i;
printf("Enter Number of Customers: ");
scanf("%d",&n);
for(i=0;i<n;i++){
    printf("Enter Customer%d Returns: ",i+1);
    scanf("%d",&cusret[i]);
    if(cusret[i]==1) returns++;
}
printf("No of Customers who Returned Exactly Once: %d",returns);}