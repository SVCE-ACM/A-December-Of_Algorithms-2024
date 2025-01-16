// Online C++ compiler to run C++ program online
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
using namespace std;


int main() {
    
    int trips=0;int n;
  cout<<"Enter number of houses:";
  cin>>n;
  vector<int> houses(n);
  
  for(int i=0;i<n;i++){
      cin>>houses[i];
  }
  int w;
  cout<<"Enter weight:";
  cin>>w;
  int i=0;
  while(i<n){
      int currseq=0;
      while(currseq+houses[i]<=w && i<n){
          
          currseq+=houses[i];i++;cout<<currseq;
          
      }
     
      trips++;
  }
  cout<<"trips:"<<trips;
    
    
    
   

    return 0;
}