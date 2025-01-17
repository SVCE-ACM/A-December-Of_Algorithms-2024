#include<stdio.h>
void main()
{
int p=1,q=0,r,i,n;
printf("Enter No of Months: ");
scanf("%d",&n);
for(i=1;i<n;i++){
    r=p;
    p=p+q;
    q=r;
    }    
printf("Plants Grown: %d",p);}