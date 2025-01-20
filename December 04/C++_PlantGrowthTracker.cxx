// December 04 - Plant Growth Tracker


#include<iostream>
#include<vector>
using namespace std;

int main()
{
	int N;
	cout<<"Enter the no of months: ";
	cin>>N;
	
	// No of the plants
	int sum=0;
	
	// Creating a vector
	vector<int> vec(N, 1);
	
	int i, value;
	for(i=2; i<N ;i++)
	{
		vec[i] = vec[i-1] + vec[i-2];
	}
	
	
	cout<<vec[i-1];
	
	
	
	
	return 0;
}


/* Solution from 1012 */