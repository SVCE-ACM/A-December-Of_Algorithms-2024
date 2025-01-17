#include<stdio.h>
void main()
{
int u=0,d=0,l=0,r=0,i;
char moves[100];
printf("Enter Moves of Robot(R,L,U,D): ");
gets(moves);
for(i=0;moves[i]!='\0';i++){
    if(moves[i]=='R') r++;
    else if(moves[i]=='L') l++;
    else if(moves[i]=='U') u++;
    else if(moves[i]=='D') d++;
}
if((r==l) && (u==d)) printf("The Robot has Returned to its Orginal Position");
else printf("The Robot has not Returned to its Orginal Position");}
 