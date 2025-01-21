#include<stdio.h>

int main()
{
	char s[100][100];
	int choice=0,i=0;
	do
	{
		printf("Enter task:");
		scanf("%c",&s[i][0]);
		getchar();
		int j=0,ch=1;
		while(ch!=0)
		{
			printf("Enter dependency:");
			scanf("%s",&s[i][j]);
			getchar();
			j++;
			printf("Do you want to enter more dependencies?");
			scanf("%d",&ch);
			getchar();
		}
		i++;
		printf("Do you want to enter more tasks?");
		scanf("%d",&choice);
	}while(choice!=0);
	
	
}