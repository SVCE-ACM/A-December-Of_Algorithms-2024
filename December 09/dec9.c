#include<stdio.h>

int main()
{
	int n=100,count=0;
	int l[n];
	for(int i=0;i<n;i++)
	{
		int num;
		scanf("%d",&num);
		if(num==-1)
		{
			break;
		}
		else
		{
			l[i]=num;
			count++;
		}
	}
	int s=0;
	for(int i=0;i<count;i++)
	{
		if(l[i]==1)
		{
			s+=1;
		}
	}
	printf("%d",s);
	
}