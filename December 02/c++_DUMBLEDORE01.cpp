#include<iostream>
using namespace std;
int main(){
	int arr[]={10, 5, 6, 3, 2, 20, 100, 80};
	int temp=0;
	int i=0;
	 int size = sizeof(arr) / sizeof(arr[0]);
     for(int i=0;i<size-1;i++)
     {
     	if(i%2==0){
     		if(arr[i]<=arr[i+1])
     		{
     			temp=arr[i];
     			arr[i]=arr[i+1];
     			arr[i+1]=temp;
			 }
		
		 }
		else
		{
			if(arr[i]>=arr[i+1])
			{
				temp=arr[i];
     			arr[i]=arr[i+1];
     			arr[i+1]=temp;
			}
		 } 
	 }
	 for(int i=0;i<size;i++){
	 	cout<<arr[i]<<",";
	 }
}
