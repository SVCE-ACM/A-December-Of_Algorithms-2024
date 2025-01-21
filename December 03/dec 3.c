#include<stdio.h>

int main()
{ 
	int r,b;
	printf("R=");
	scanf("%d",&r);
	printf("B=");
	scanf("%d",&b);
	
	if((r-b)>1)
	{
		printf("Not possible!\n");
	}
	else if((b-r)>1)
	{
		printf("Not possible\n");
	}
	else
	{
		for(int i=0;i<r+b;i++)
		{
			if(r>b)
			{
			if(i%2==0)
			{
				printf("R");
			}
			else
			{
				printf("B");
			}
		}
		else
		{
			if(i%2==0)
			{
				printf("B");
			}
			else
			{
				printf("R");
			}
		}
		}
	}
}