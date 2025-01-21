#include<stdio.h>

int main()
{
	int first=1,third;
	int second = 1;
	int n;
	printf("No of Months:");
	scanf("%d",&n);
	for(int i=2;i<n;i++)
	{
		third = first+second;
		int temp;
		temp=second;
		second=third;
		first=temp;
	}
	printf("%d",third);
}