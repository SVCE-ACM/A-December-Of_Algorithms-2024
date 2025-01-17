
#include <iostream>
using namespace std;
#include<vector>
int main() {
    int n;
    cout << "Enter the size of the vector: ";
    cin >> n;
    vector<vector<int>> ans;
    ans.push_back({1});
    for (int i=1;i<=n;i++){
        vector<int> temp;
        int x=0;
        while(x<=i){
            int sum=0;
            if (x < ans[i - 1].size()) {
                sum += ans[i - 1][x];
            }
            if (x - 1 >= 0) {
                sum += ans[i - 1][x - 1];
            }
            
            temp.push_back(sum);x++;
        }
        ans.push_back(temp);
        }
        
    
    for(int i=0;i<n;i++){
        for(int j=0;j<ans[i].size();j++){
            cout<<ans[i][j]<<"\t";
        }
        cout<<"\n";
    }
   
    return 0;
}