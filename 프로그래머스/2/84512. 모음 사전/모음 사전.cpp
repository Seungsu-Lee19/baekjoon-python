#include <string>
#include <vector>

using namespace std;

int n, ans = 0;
string answer;
char alpha[5] = {'A', 'E', 'I', 'O', 'U'};

int cnt = 1;

void dfs(int depth, string& words){
    if(depth == 5) return;
    if(ans != 0) return;
    
    for(int i = 0; i < 5; i++){
        words += alpha[i];
        
        if(words == answer) {
            ans = cnt;
        }
        
        cnt++;
        
        dfs(depth + 1, words);
        
        words.pop_back();
    }
}

int solution(string word) {
    n = word.length();
    answer = word;
    
    string a = "";
    dfs(0, a);
    
    return ans;
}