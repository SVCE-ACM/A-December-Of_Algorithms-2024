#include<stdio.h>

int main()
{
	int n;
	scanf("%d",&n);
	int a[n];
	for(int i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	int j,min,index,count=0;
	for(int i=0;i<n;i++)
	{
		min=a[i];
		index=i;
		for(int j=i+1;j<n;j++)
		{
			if(a[j]<min)
			{
				min=a[j];
				index=j;
			}
		}
		if(min!=a[i])
		{
		int temp;
		temp=a[i];
		a[i]=min;
		a[index]=temp;
		count++;
		}
	}
	printf("%d",count);
}