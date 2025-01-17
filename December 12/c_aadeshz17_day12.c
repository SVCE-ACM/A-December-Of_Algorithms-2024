#include<stdio.h>
#include<string.h>
void main()
{
int i,n,custno,custickets[100];
char customer[100][100],vip[3]="VIP";
printf("Enter No of Tickets Available: ");
scanf("%d",&n);
printf("Enter No of Customers: ");
scanf("%d",&custno);
printf("Enter Customer Name followed by VIP, if they are VIP\n");
for(i=0;i<custno;i++){
    printf("Enter Customer %d Name: ",i+1);
    scanf(" %[^\n]s",customer[i]);
    printf("Enter Customer %d Tickets: ",i+1);
    scanf("%d",&custickets[i]);
}
for(i=0;i<custno;i++){
    if(strstr(customer[i],vip) && n>0){
        if(custickets[i]<=n){
            n-=custickets[i];
            printf("%s was served %d Tickets\n",customer[i],custickets[i]);}
        else{
            printf("%s was served %d Tickets\n",customer[i],n);
            n=0;}
        custickets[i]=0;}
}
for(i=0;i<custno;i++){
    if(n>0){
        if(custickets[i]<=n && custickets[i]>0){
            n-=custickets[i];
            printf("%s was served %d Tickets\n",customer[i],custickets[i]);}
        else{
            printf("%s was served %d Tickets\n",customer[i],n);
            n=0;}
        custickets[i]=0;}
}
for(i=0;i<custno;i++)
    if(custickets[i]!=0) 
        printf("%s was not served Tickets\n",customer[i]);
}
 