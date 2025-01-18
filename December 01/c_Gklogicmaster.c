#include <stdio.h>

int main() {
    int n;
    printf("enter the numberof particapants :");
    scanf("%d",&n);
    int a[n-1],m;
    printf("enter the bib numbers :");
    for(m=0;m<n;m++){
        scanf("%d",&a[m]);
    }
    printf("the bib numbers present is :");
    printf("{");
    for(m=0;m<n;m++){
        printf("%d ",a[m]);
    }
    printf("}");
    int u=0;
    for(m=0;m<n;m++){
        u=u+a[m];
    }
    u=u+1;
    int y=0;
    for(m=1;m<=n;m++){
        y=y+m;
    }
    printf("\nthe bib number absent is :{%d}",u-y);
    
return 0;
}
