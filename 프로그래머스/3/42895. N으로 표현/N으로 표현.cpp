#include <vector>
#include <unordered_set>

using namespace std;

int solution(int N, int number) {
    vector<unordered_set<long long>> dp(9);

    long long repeat = 0;
    for(int cnt = 1; cnt < 9; cnt++){
        repeat = repeat * 10 + N;
        dp[cnt].insert(repeat);
        
        for(int left = 1; left < cnt; left++){
            int right = cnt - left;
            
            for(long long a: dp[left]){
                for(long long b: dp[right]){
                    dp[cnt].insert(a + b);
                    dp[cnt].insert(a - b);
                    dp[cnt].insert(a * b);
                    
                    if(b != 0) dp[cnt].insert(a / b);
                }
            }
        }
        
        if(dp[cnt].find(number) != dp[cnt].end()) return cnt;
    }

    return -1;
}