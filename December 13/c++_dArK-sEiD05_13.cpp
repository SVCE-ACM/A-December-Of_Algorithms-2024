#include <iostream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

void swap(vector<int>& arr, int i, int j)
{
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}



int minSwaps(vector<int> arr, int N)
{
    int ans = 0;
    vector<int> temp = arr;

    
    map<int, int> h;

    sort(temp.begin(), temp.end());
    for (int i = 0; i < N; i++) {
        h[arr[i]] = i;
    }
    for (int i = 0; i < N; i++) {
    
      
        if (arr[i] != temp[i]) {
            ans++;
            int init = arr[i];

            swap(arr, i, h[temp[i]]);

            h[init] = h[temp[i]];
            h[temp[i]] = i;
        }
    }
    return ans;
}


int main()
{   int n;
    cout<<"Enter length:";
    cin>>n;
    vector<int> a(n);
    cout<<"Enter elements:";
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
   
    cout << minSwaps(a, n);
}
