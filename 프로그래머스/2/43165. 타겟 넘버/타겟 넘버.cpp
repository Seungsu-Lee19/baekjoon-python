#include <string>
#include <vector>

using namespace std;

int N;
int ans = 0;
int t;

vector<int> grid;

void dfs(int x, int sum){
    if(x == N) {
        if(sum == t) ans++;
        
        return;
    }
    
    dfs(x + 1, sum + grid[x]);
    dfs(x + 1, sum - grid[x]);
}

int solution(vector<int> numbers, int target) {
    N = numbers.size();
    grid = numbers;
    t= target;
    
    dfs(0, 0);
    return ans;
}