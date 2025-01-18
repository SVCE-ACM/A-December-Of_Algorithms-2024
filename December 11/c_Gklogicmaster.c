#include<stdio.h>
#include<string.h>
int main(){
    int x=0,y=0;
    int i,size;
    char moves[20];
    printf("enter the moves to move ('U,D,R,L'):");
    scanf("%s",moves);
    size=strlen(moves);
    for(i=0;i<size;i++){
        if(moves[i]=='R'){
            x+=1;
        }
        else if(moves[i]=='L'){
            x-=1;
        }
        else if(moves[i]=='U'){
            y+=1;
        }
        else if(moves[i]=='D'){
            y-=1;
        }
        else{
            printf("enter valid moves\n");
        }
        
    }
    if(x==0 && y==0){
        printf("true");
    }
    else{
        printf("false");
    }
    return 0;
}
