#include<stdio.h>

int Joseph(int n,int k)
{
	if(n==1)
	{
		return 1;
	}
	else
	{
		return (Joseph(n-1,k)+k-1)%n+1;
	}
}
int main()
{
	int front,rear;
	front=rear=-1;
	int n;
	scanf("%d",&n);
	int k;
	scanf("%d",&k);
	printf("Safe position is:%d",Joseph(n,k));
}