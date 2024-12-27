(1) The Vanishing Number-missing num
#include<stdio.h>
int N,arr[100],i,j,m;
int main(){
    printf("enter number of participants:");
    scanf("%d",&N);
    for(i=0;i<N-1;i++){
        printf("enter bib number:");
        scanf("%d",&arr[i]);
    }
    for(i=1;i<N;i++){
        int count=0;
        for(j=0;j<N-1;j++){ 
            if(arr[j]==i) count=1;
        }
        if(count==0) m=i;
    }printf("missing bib number= %d",m);
    return 0;
}
