#include<bits/stdc++.h>
using namespace std;
int main(){
    int n , m , s;
    cin>>n>>m>>s;
    int visited[n + 1];
    vector <int>  Graph[n+1];
    for(int i =0 ; i<n + 1 ; i++){
        visited[i] = 0;
    }
    int a , b;
    for(int i = 0; i < m; i++){
        cin>>a>>b;
        Graph[a].push_back(b);
    }
   
    /*for (int i=1 ; i< n+1 ; i++){
        cout<<i;    
        for (int j =0 ; j< Graph[i].size() ; j++){
            cout<<Graph[i][j]<<" ";
        }
        cout<<endl;
    }*/
    int count = 0;
    bool flag = true;
    for(int i = 0 ; i < n+1; i++ ){
        queue < int > QUEUE;
        if(i == 0){
            QUEUE.push(s);
            visited[s] = s;
            while((QUEUE.size())!= 0){
                for(int j=0; j<(Graph[QUEUE.front()].size()) ; j++){
                    if(visited[Graph[QUEUE.front()][j]] != s){
                        QUEUE.push(Graph[QUEUE.front()][j]);
                        visited[Graph[QUEUE.front()][j]] = s;
                    }
                }
            QUEUE.pop();
            }
        }
        else{
            if(visited[i] == 0){    
                QUEUE.push(i);
                visited[i] = i;
            }
            while((QUEUE.size())!= 0){
                for(int j=0; j<(Graph[QUEUE.front()].size()) ; j++){
                    if(visited[Graph[QUEUE.front()][j]] != i and visited[Graph[QUEUE.front()][j]] != s){
                        QUEUE.push(Graph[QUEUE.front()][j]);
                        visited[Graph[QUEUE.front()][j]] = i;
                    }
                }
            QUEUE.pop();
            }
        }
    }
    set <int> SET;
    for(int i=1; i<n+1; i++){
        //cout<<visited[i]<<' ';
        SET.insert(visited[i]);
    }
    cout<<SET.size()-1;
}