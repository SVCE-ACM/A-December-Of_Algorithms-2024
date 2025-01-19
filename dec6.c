//(6) Target Pair Finder:
#include<stdio.h>
int main(){
    int i,n,sum,a[100];
    printf("enter num of elements:");
    scanf("%d",&n);
    for(i=0;i<n;i++){
        printf("enter val:");
        scanf("%d",&a[i]);
    }
    printf("enter target sum:");
    scanf("%d",&sum);
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(a[i]+a[j]==sum){
                printf("(%d,%d) ",a[i],a[j]);
            }
        }
    }printf("\n");
    return 0;
}

