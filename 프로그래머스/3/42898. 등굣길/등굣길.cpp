#include <string>
#include <vector>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    const long long div = 1000000007;
    int answer = 0;
    
    vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, -1));
    vector<vector<bool>> water(n + 1, vector<bool>(m + 1));
    
    for(const auto& p: puddles){
        int y = p[0];
        int x = p[1];
        water[x][y] = true;
    }
    for(int i = 1; i <= n; i++){
        if(water[i][1]) break;
        dp[i][1] = 1;
    }
    for(int i = 1; i <= m; i++){
        if(water[1][i]) break;
        dp[1][i] = 1;
    }
    
    for(int i = 2; i <= n; i++){
        for(int j = 2; j <= m; j++){
            if(water[i][j]) continue;
            
            if(dp[i - 1][j] != -1 && dp[i][j - 1] != -1) dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % div;
            else if(dp[i - 1][j] != -1){
                dp[i][j] = dp[i - 1][j] % div;
            }
            else if(dp[i][j - 1] != -1){
                dp[i][j] = dp[i][j - 1] % div;
            }
        }
    }
    
    if(dp[n][m] == -1) dp[n][m] = 0;
    return dp[n][m];
}