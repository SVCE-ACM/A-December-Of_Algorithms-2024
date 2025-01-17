#include<stdio.h>
void main(){
int arr[100],i,temp,n;
printf("Enter Number of Fans: ");
scanf("%d",&n);
for(i=0;i<n;i++){
    printf("Enter Fan%d Height: ",i+1);
    scanf("%d",&arr[i]);}
for(i=0;i<n;i++){
    if(i%2==0){
        if(arr[i]<arr[i+1]){
            temp=arr[i];
            arr[i]=arr[i+1];
            arr[i+1]=temp;}
        }    
    else{
        if(i==n-1)
            break;
        if(arr[i]>arr[i+1]){
            temp=arr[i];
            arr[i]=arr[i+1];
            arr[i+1]=temp;}
        }    
    }
printf("Arranged Fans: {");
for(i=0;i<n-1;i++)
    printf("%d,",arr[i]);      
printf("%d}",arr[n-1]);
}