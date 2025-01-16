#include <iostream>
using namespace std;

int main() {
    int n;
    cout<<"Enter months:";
   cin>>n;
   int i=1;int a=1;int b=1;
   if(n==1 || n==2){cout<<1;}
   while(i<=n-2){
       int c=a+b;a=b;b=c;i++;
   }
   cout<<b;
    return 0;
}