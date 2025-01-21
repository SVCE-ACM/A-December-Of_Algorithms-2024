#include<iostream>
using namespace std;
int main(){
	int n=10;
	int a=0;
	int b=1;
	int c=0;
	for(int i=0;i<n-1;i++)
	{
		c=a+b;
		a=b;
		b=c;
	}
	cout<<c;
}
