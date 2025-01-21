#include<iostream>
using namespace std;
int main(){
	int returns[]={2,1,5,1,0,3,1,4,1};
	int i=0;
	int result=0;
	int size=sizeof(returns)/sizeof(returns[0]);
	while(i<size)
	{
		if(returns[i]==1)
		{
			result++;
		}
		i++;
	}
	cout<<result;
}
