#include<iostream>
using namespace std;
int main(){
	int result=0;
	int n=5;
	int array[]={1,2,4,5};
	for(int i=0;i<n;i++){
		if(array[i]!=i+1)
		{
			result=i+1;
			break;
		}
		
	}
	cout<<result;
}
