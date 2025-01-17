#include<stdio.h>
int cost=0;
void swap(int *a,int *b){
    int temp=*a;
    *a=*b;
    *b=temp;
    cost++;}
int min(int arr[],int p,int n){
    int i,j,temp=arr[p];
    for(i=p;i<n;i++)
        if(arr[i]<temp) j=i;
    return j;}
void main()
{
int i,j,temp,n,arr[100];
printf("Enter No of Elements: ");
scanf("%d",&n);
for(i=0;i<n;i++){
    printf("Enter Elements %d: ",i+1);
    scanf("%d",&arr[i]);}
for(i=0;i<n-1;i++){
    j=min(arr,i,n);
    if(j!=i) swap(&arr[i],&arr[j]);}
        printf("Minimum Cost: %d",cost);
}