#include<iostream>
#include<cstdlib>
using namespace std;
int main()
{
	int B=3;
	int R=3;
	int i=0;
	string arr[B+R];

    if (!(B - R <= 1 || R - B <= 1))
	{
		cout<<"Not possible";
	}
	else{
		if(B>R){
			for(int i=0;i<B+R;i++)
			{
				if(i%2==0)
				{
					arr[i]="B";
				}
				else{
					arr[i]="R";
				}
			}
		
		}
		else{
			for(int i=0;i<B+R;i++)
			{
				if(i%2==0)
				{
					arr[i]="R";
				}
				else{
					arr[i]="B";
				}
			}
	}
	
}
for(int i=0;i<B+R;i++)
{
	cout<<arr[i]<<" ";
}
}
