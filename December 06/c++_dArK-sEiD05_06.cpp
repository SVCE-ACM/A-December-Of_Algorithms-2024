// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
#include <vector>
#include <unordered_map>
int main() {
    int n;
    cout << "Enter the size of the vector: ";
    cin >> n;

    vector<int> vec(n); 
    cout<<"Enter target:";
    int tar;
    cin>>tar;

    cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; i++) {
        cin >> vec[i];
    }

    vector<pair<int, int>> pairs;
    unordered_map<int,int> hm;
    for(int i=0;i<n;i++){
        hm[vec[i]]++;
    }
    for(int i=0;i<n;i++){
        if(hm.find((tar-vec[i]))!=0 && hm[abs(vec[i]-tar)]>0){
            if(vec[i]*2==tar){
                if(hm[vec[i]]>1){
                    pairs.push_back({vec[i],(tar-vec[i])});
                    hm.erase(vec[i]);
                    
                }
            }else{
            pairs.push_back({vec[i],(tar-vec[i])});
            hm[vec[i]]--;hm[vec[i]-tar]--;
        }}
    }
    for (const auto& p : pairs) {
        cout << "(" << p.first << ", " << p.second << ")" << endl;
    }
   
    return 0;
}