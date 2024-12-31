//(11) The Robot Returns
#include<stdio.h>
#include<string.h>
int main(){
    char path[100];
    printf("enter path:");
    scanf("%s",&path);
    int count=0,i=strlen(path);
    while(i!=-1){
        if(path[i]=='u') count=count+1;
        else if(path[i]=='d') count=count-1;
        else if(path[i]=='r') count=count+2;
        else if(path[i]=='l') count=count-2;
        i=i-1;
    }
    if(count==0) printf("robot came to original position");
    else printf("robot didn't reach it's original position");
}
