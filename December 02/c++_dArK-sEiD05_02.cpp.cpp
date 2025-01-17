
#include <iostream>
#include <vector>
using namespace std;
int main() {
    // Write C++ code here
    vector <int> arr= {10, 5, 6, 3, 2, 20, 100}
;
    
  
    for (int i = 1; i < arr.size(); i += 2) {
     
        if(arr[i - 1] < arr[i]) {
            swap(arr[i - 1], arr[i]);
        }
      
        if(i+1<arr.size()&&arr[i]>arr[i + 1]) {
            swap(arr[i], arr[i + 1]);
        }
    }
  
    
    
    for(int i=0;i<arr.size();i++){
        cout<<arr[i]<<"\t";
    }
    
   

    return 0;
}