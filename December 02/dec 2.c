#include<stdio.h>

int main()
{
	int n,count;
	scanf("%d",&n);
	int a[n];
	for(int i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(int i=0;i<n;i++)
	{
		count=i;
			if(count%2==0)
			{
				if(a[i]<a[i+1])
				{
					int temp;
					temp=a[i];
					a[i]=a[i+1];
					a[i+1]=temp;
				}
			}
	}
	for(int i=0;i<n;i++)
	{
		printf("%d \t",a[i]);
	}
}