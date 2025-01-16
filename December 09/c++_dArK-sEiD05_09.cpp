// Online C++ compiler to run C++ program online
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
using namespace std;


int main() {
    
  int n;
  cout<<"Enter number of elements:";
  cin>>n;
  vector<int> vec(n);
  
  for(int i=0;i<n;i++){
      cin>>vec[i];
  }
  int cnt=0;
  for(int i=0;i<vec.size();i++){
      if(vec[i]==1){
          cnt++;
      }
  }
  cout<<"Occurance"<<cnt;
    
    
    
   

    return 0;
}