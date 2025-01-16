
#include <iostream>
using namespace std;

int main() {
    
    int n,k;
    cout<<"Enter persons:";
   cin>>n;
   cout<<"Enter k:";
   cin>>k;
   int i=1;int ans=0;
   while(i<=5){
       ans=(ans+k)%i;
       i++;
   }
   cout<<ans+1;
   
    return 0;
}