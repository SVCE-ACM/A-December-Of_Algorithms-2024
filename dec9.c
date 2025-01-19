//(9) customer return frequency:
#include<stdio.h>
int main(){
    int num,arr[100],count=0,i;
    printf("enter number of customers:");
    scanf("%d",&num);
    for(i=0;i<num;i++){
        printf("enter number to times an item was returned:");
        scanf("%d",&arr[i]);
    }
    for(i=0;i<num;i++) if(arr[i]==1) count=count+1;
    printf("num of customers who returns item once:%d\n",count);
    return 0;
}

