//(13) minimum swap sorting problem-Selection sort
#include<stdio.h>
int s=0;
void swap(int *a,int *b){
    int temp=*a;
    *a=*b;
    *b=temp;
    s=s+1;
}
int min(int arr[],int n,int m){
    int i,small=1000,j;
    for(i=n;i<m;i++){
        if(arr[i]<small){ 
            small=arr[i];
            j=i;
        }
    } return j;
}
int main(){
    int arr[100],size,i,j,n;
    printf("enter num of elements:");
    scanf("%d",&size);
    for(i=0;i<size;i++){
        printf("enter element:");
        scanf("%d",&arr[i]);
    }
    for(i=0;i<size;i++){
        int m=min(arr,i,size);
        if(m!=i) swap(&arr[m],&arr[i]);
    }printf("cost=%d",s);
    return 0;
}

