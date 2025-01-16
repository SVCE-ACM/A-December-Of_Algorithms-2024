#include <iostream>
using namespace std;
int main() {
    // Write C++ code here
   int r,b;
   cout<<"Enter red boxes:";
   cin>>r;
   cout<<"Enter blue boxes:";
   cin>>b;cout<<r<<b<<abs(r-b);
   if(abs(r-b)==1){
       cout<<"Not possible";
   }
   else{
       cout<<"Possible";
   }

    return 0;
}