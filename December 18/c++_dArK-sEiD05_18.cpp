// Online C++ compiler to run C++ program online
#include <iostream>
#include <string>
using namespace std;
int main() {
    // Write C++ code here
    string str="RDEREDR";int start;int end;int max=-1;
    for(int i=0;i<(str.size());i++){
        int k=i;int j=i;int mid=0;int curr=1;
        while(k>=0 && j<(str.size()) ){
            
            if(str[k]==str[j] ){
                curr+=2;
                if(curr>max){
                    start=k;end=j;mid=i;max=curr;
                }
                
            }
            k--;j++;
        }
    }
    
    int sum=0;
    for(int i=start;i<=end;i++){
        if(str[i]=='D')
            sum+=500;
        
        else if(str[i]=='R')
        sum+=250;
        else if(str[i]=='E')
        sum+=100;
    }
    
    cout<<sum*(end-start+1);
    return 0;
}