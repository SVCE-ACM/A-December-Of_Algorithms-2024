// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
#include<vector>
int main() {
    int n;
    cout << "Enter the size: ";
    cin >> n;int i=1;int sum=0;
    while(i<=n){
        int k=i;
        while(k>0){
            int x=k%10;
            sum+=x*x;
            k=k/10;
        }
        i++;
    }
    cout<<sum;
    
   
    return 0;
}