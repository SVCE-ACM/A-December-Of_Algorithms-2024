//(7) The Magical Tower-pascals triangle:
#include<stdio.h>
int main(){
    int n,a[100][100];
    printf("enter number of rows:");
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=i;j++){
            if(j==1||j==i) a[i][j]=1;
            else a[i][j]=a[i-1][j]+a[i-1][j-1];
        }
    }
    for(int i=1;i<=n;i++){ 
        for(int j=1;j<=i;j++){ 
            printf("%d ",a[i][j]);
        }printf("\n");
    }
    return 0;
}

