//(3) Alternating Square Arrangement
#include<stdio.h>
int main(){
    int r,b,i;
    printf("enter number of red squares:");
    scanf("%d",&r);
    printf("enter number of blue squares:");
    scanf("%d",&b);
    if(r%2==0&&b%2==0) printf("not possible");
    else{
        if(r>b){ 
            printf("r");
            for(i=1;i<=b;i++) printf("br");
        }
        else{
            printf("b");
            for(i=1;i<=r;i++) printf("rb");            
        }
    }
    return 0;
}
