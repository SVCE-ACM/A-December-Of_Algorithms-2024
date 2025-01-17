#include<stdio.h>
void main(){
int arr[100],i,j,n,flag;
printf("Enter Number of Participants: ");
scanf("%d",&n);
for(i=0;i<n-1;i++){
    printf("Enter Participant%d Number: ",i+1);
    scanf("%d",&arr[i]);}
for(j=1;j<=n;j++){
    flag=0;
    for(i=0;i<n;i++){
        if(arr[i]==j){
            flag=1;
            break;}
    }
    if(flag==0){
        printf("Missing Participant Number: %d",j);
        break;}
}
}