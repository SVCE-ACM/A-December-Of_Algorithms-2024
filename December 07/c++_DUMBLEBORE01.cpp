#include<iostream>
using namespace std;
int main(){
	const int floor=5;
	int tower[floor][floor]={0};
	tower[0][0]=1;
	for(int i=0;i<floor;++i)
	{
		tower[i][0]=1;
		for(int j=1;j<i;++j)
		{
			tower[i][j]=tower[i-1][j-1]+tower[i-1][j];
		}
		tower[i][i]=1;
	}
	for(int i=0;i<floor;++i)
	{
		for(int j=0;j<floor;++j)
		{   if(tower[i][j]!=0){
			cout<<tower[i][j]<<"";
		}
	}
		cout<<endl;
	}
	
}
