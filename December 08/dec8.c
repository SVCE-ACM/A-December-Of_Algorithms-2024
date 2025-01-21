#include<stdio.h>

int main()
{
	int n,i;
	scanf("%d",&n);
	int r,s=0;
	for(i=1;i<=n;i++)
	{
		int num;
		num=i;
		while(num>0)
		{
		r = num%10;
		s+=r*r;
		num=num/10;
	}
	}
	printf("Sum is:%d",s);
	
}