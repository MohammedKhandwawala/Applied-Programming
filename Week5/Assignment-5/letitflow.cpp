#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    for(int k=0 ; k<t ; k++){
        int n;
        cin>>n;
        char a[n],b[n],c[n];
        for(int i =0 ; i<n ; i++){
            cin>>a[i];
        }
        for(int i =0 ; i<n ; i++){
            cin>>b[i];
        }
        for(int i =0 ; i<n ; i++){
            cin>>c[i];
        }
        int ans = 1;
        if((a[0] =='.' and b[0] == '.') and (b[n-1]=='.' and c[n-1]=='.') and (n%2 == 0)){
            for(int i=1 ; i<n-1 ; i++){
                if(i%2!=0){
                    if((a[i]=='#' and c[i+1]=='#') or (a[i]=='#' and c[i+1]=='#')){
                        ans = (ans*1)%1000000007;
                    }
                    else if((a[i] == '.') and (a[i+1] == '.') and (c[i]=='.') and (c[i+1] == '.')){
                        ans = (ans*2)%1000000007;
                    }
                    else if((a[i] == '#') and a[i+1] == '.' and c[i] == '.' and c[i+1] == '.'){
                        ans = (ans*1)%1000000007;
                    }
                    else if((a[i+1] == '#') and a[i] == '.' and c[i] == '.' and  c[i+1] == '.'){
                        ans = (ans*1)%1000000007;
                    }
                    else if((c[i] == '#') and a[i+1] == '.' and a[i] == '.' and c[i+1] == '.'){
                        ans = (ans*1)%1000000007;
                    }
                    else if((c[i+1] == '#') and a[i+1] == '.' and c[i] == '.' and  a[i] == '.'){
                        ans = (ans*1)%1000000007;
                    }
                    else{
                        ans = 0;
                    }
                }
                else if((a[i]=='#' and c[i]=='#') or (a[i]=='#' and c[i]=='#')){
                        ans= 0;
                }
                else if(b[i]=='#'){
                    ans = 0;
                }
            }
            cout<<"Case #"<<k+1<<": "<<ans<<endl;
        }
        else{
            cout<<"Case #"<<k+1<<": 0"<<endl;
        }
    }
}