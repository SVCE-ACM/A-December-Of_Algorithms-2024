#include<stdio.h>
void swap(int *a,int *b){
    int temp;
    temp=*a;
    *a=*b;
    *b=temp;
}
    

void wave_sort(int arr[],int n){
    for(int i=0;i<n;i+=2){
        if(arr[i]<arr[i+1]){
            swap(&arr[i],&arr[i+1]);
        }
        if(i>0 && arr[i]<arr[i-1]){
            swap(&arr[i-1],&arr[i]);
        }
    }
    
}
int main(){
    int n,i;
    printf("enter the no of elements :");
    scanf("%d",&n);
    int arr[n];
    printf("enter the elements to wave sort :");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    printf("the unsorted array is : ");
     printf("{");
    for(i=0;i<n;i++){
    printf("%d,",arr[i]);
    }
    printf("}");
    wave_sort(arr,n);
     printf("\nthe wave sorted array is : ");
     printf("{");
    for(i=0;i<n;i++){
    printf("%d,",arr[i]);
    }
    printf("}");
    
    return 0;
}
