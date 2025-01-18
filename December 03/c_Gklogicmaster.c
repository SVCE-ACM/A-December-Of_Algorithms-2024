#include<stdio.h>
int main (){
    int R,B,i,j;
    printf("enter the number of red squares:");
    scanf("%d",&R);
    printf("enter the number of blue squares:");
    scanf("%d",&B);
    if(R-B == 1 || B-R ==1){
       while(B>0 || R>0){
           if(B>R){
               if(B>0){
                   printf("B");
                   B--;
                   
               }
               if(R>0){
               printf("R");
               R--;}}
            if(R>B){
                if(R>0){
                    printf("R");
                    R--;
                }
                if(B>0){
                    printf("B");
                    B--;
                }
            }
    }}
    else{
        printf("NOT POSSIBLE");
    }
    return 0;
    
}
