#include<stdio.h>
#include<stdlib.h>
#include<string.h.h>
void main(){
int i=0,r,b;
char dominant,secondary,squares[100];
printf("Enter Number of Red Squares: ");
scanf("%d",&r);
printf("Enter Number of Blue Squares: ");
scanf("%d",&b);
if(abs(r-b)>1){
    printf("Not Possible for Alternative Squares");}
else{
    char dominant = (r >= b) ? 'R' : 'B';
    char secondary = (r >= b) ? 'B' : 'R';
    int domcount = (r >= b) ? r : b;
    int seccount = (r >= b) ? b : r;
    while(domcount>0 || seccount>0){
        if(domcount>0){
        squares[i++]=dominant;
        domcount--;}
        if(seccount>0){
        squares[i++]=secondary;
        seccount--;}
    }
    printf("%s",squares);}
}