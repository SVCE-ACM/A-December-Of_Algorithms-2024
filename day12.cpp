// Online C++ compiler to run C++ program online
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
using namespace std;
vector<string> splitStringBySpace(const string &str) {
    vector<string> tokens;
    stringstream ss(str);
    string word;

   
    while (ss >> word) {
        tokens.push_back(word);
    }
    return tokens;
}

int main() {
    
    
    vector<string> ans;
    
    vector<string> arr={"Eve 4","Diana 3 VIP","Adam 5","Frank 6 VIP"};
    
   int total;
   cout<<"Enter total tickets";
   cin>>total;bool visited[arr.size()]={false};
    for(int i=0;i<arr.size();i++){
        if(total>0){
       vector<string> result = splitStringBySpace(arr[i]);
       if(result[result.size()-1]=="VIP"){
           string userw=result[1];int a=stoi(userw);
           if(a>total){userw=to_string(total);}
           string str=result[0]+" purchased "+userw+" tickets";
           ans.push_back(str);
           total-=stoi(userw);
          visited[i]=true;
       }
    }else{break;}}
    for(int i=0;i<arr.size();i++){
         vector<string> result = splitStringBySpace(arr[i]);
        if(total>0){
      
       if(result[result.size()-1]!="VIP"){
           string userw=result[1];int a=stoi(userw);
           if(a>total){userw=to_string(total);}
           string str=result[0]+" purchased "+userw+" tickets";
           ans.push_back(str);
           total-=stoi(userw);visited[i]=true;
           
       }
    }else{
      break;
        
    }}
    for(int i=0;i<arr.size();i++){
        if(visited[i]==false){ 
            vector<string> result = splitStringBySpace(arr[i]);
            
            string str=result[0]+" no tickets ";
           ans.push_back(str);}
    }
    
    for(int i=0;i<ans.size();i++){
        cout<<ans[i]<<"\n";
    }
   
    
    
   

    return 0;
}