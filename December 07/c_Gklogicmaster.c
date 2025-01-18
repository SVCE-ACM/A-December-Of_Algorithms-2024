#include<stdio.h>
int main(){
    int num_row;
    printf("enter the number of rows :");
    scanf("%d",&num_row);
    int i,j,k;
    printf("[");
    for(i=0;i<num_row;i++){
        printf("[");
        for(j=0;j<=i;j++){
            if(j==0){
                printf(" 1 ");
            }
            else if(j==i){
                printf(" 1 ");
            }
            else{
                int num=1;
                for(k=1;k<=j;k++){
                    num=num*(i-k+1)/k;
                }
                printf(" %d ",num);
            }
            }
            printf("]\n");
        }
        printf("]");
        return 0;
    }
