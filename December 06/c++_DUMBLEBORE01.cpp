#include <iostream>
using namespace std;
int main() {
    int arr[] = {10,15,3,7,8,12,5};
    int n = sizeof(arr)/sizeof(arr[0]);
    int target = 20;
    std::cout << "Pairs: ";
    cout<<"[";
        for(int i = 0; i < n; i++) {
            for(int j = i ; j < n; j++) {
                if(arr[i] + arr[j] == target) {
                    cout <<"(" << arr[i] << "," << arr[j] << ")";
                }
            }
        }
        cout<<"]";
           cout << "\n";
    
    return 0;
}
