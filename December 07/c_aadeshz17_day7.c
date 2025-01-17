#include<stdio.h>
void main()
{
int r,value,i,j;
printf("Enter No of Rows: ");
scanf("%d",&r);
printf("[");
for(i=0;i<r; i++){
        int value = 1;
        printf("[");
        for (int j=0;j<=i-1;j++){
            printf("%d,",value);
            value=value*(i-j)/(j+1); 
        }
        printf("%d],",value);
    }
printf("]");}