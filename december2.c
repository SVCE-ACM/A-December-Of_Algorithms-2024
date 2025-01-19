//(2) The Wave Sort Challenge-><><:
#include<stdio.h>
void swap(int *x,int*y){
    int t=*x;
    *x=*y;
    *y=t;
}
int main(){
    int n,i,arr[100];
    printf("enter num of fans:");
    scanf("%d",&n);
    for(i=0;i<n;i++){
        printf("enter height %d:",i+1);
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++){
        if(i%2==0){
            if(arr[0+i]<arr[1+i]) swap(&arr[0+i],&arr[1+i]);
            if(arr[1+i]>arr[2+i]) swap(&arr[1+i],&arr[2+i]);
        }
    }
    for(i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
    return 0;
}

