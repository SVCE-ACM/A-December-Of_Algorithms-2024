#include<iostream>
using namespace std;
int main(){
	int n=12;
	int pow=1;
	int sum=0;
	int m=0;
	for(int i=1;i<=n;i++)
	{
	int temp=i;
	while(temp>0)
		{
		m=temp%10;
		sum=sum+m*m;
		temp=temp/10;
	}
}

	cout<<sum;
}
