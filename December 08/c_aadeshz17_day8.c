#include<stdio.h>
void main()
{
int n,r,sum=0,i,j;
printf("Enter Number: ");
scanf("%d",&n);
for(i=1;i<=n;i++){
    j=i;
    while(j!=0){
        r=j%10;
        sum=sum+(r*r);
        j/=10;}
}
printf("%d",sum);}