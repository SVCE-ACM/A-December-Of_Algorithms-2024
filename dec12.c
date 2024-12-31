//(12) Smart Ticketing System
#include<stdio.h>
#include<string.h>
int main(){
    char name[100][100],*vip="vip";
    int ticket[100],n,i,tot;
    printf("enter num of person:");
    scanf("%d",&n);
    printf("enter tot tickets avalible:");
    scanf("%d",&tot);
    for(i=0;i<n;i++){
        printf("enter name followed by vip if they are a vip:");
        scanf("%s",name[i]);
        printf("enter number of tickets they wanted:");
        scanf("%d",&ticket[i]);
    }
    for(i=0;i<n;i++){
    if(tot>0&& strstr(name[i],vip)!=NULL){ 
        if(ticket[i]<=tot){
            tot=tot-ticket[i];
            printf("%s was served with %d tickets\n",name[i],ticket[i]);
        }else{
            printf("%s was served with %d tickets\n",name[i],tot);
            tot=0;  
        }ticket[i]=0;
    }if(tot<=0) break;
    }
    for(i=0;i<n;i++){
        if(tot>0&& strstr(name[i],vip)==NULL){
            if(ticket[i]<=tot){
                tot=tot-ticket[i];
                printf("%s was served with %d tickets\n",name[i],ticket[i]);
            }else{
                printf("%s was served with %d tickets\n",name[i],tot);
                tot=0;  
            }ticket[i]=0;
        }if(tot<=0) break;
    } 
    for(i=0;i<n;i++) if(ticket[i]!=0) printf("%s was not served\n",name[i]);
}
