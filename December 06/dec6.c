#include<stdio.h>

int main()
{
	int n=100,sum;
	int list[n],count=0,l[100][2];
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
			list[i]=num;
			count++;
		}
	}
	printf("Target sum:");
	scanf("%d",&sum);
	int k=0;
	for(int i=0;i<count;i++)
	{

		for(int j=i+1;j<count;j++)
		{
			if(list[i]+list[j]==sum)
			{
				l[k][0]=list[i];
				l[k][1]=list[j];
				k++;
			}
		}
	}	
	for(int i=0;i<k;i++)
	{
		printf("(%d,%d)\t",l[i][0],l[i][1]);
	}
}