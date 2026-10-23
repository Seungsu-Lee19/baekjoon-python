#include <vector>
#include <array>
#include <algorithm>

using namespace std;

int solution(vector<int> money) {
    int n = money.size();
    vector<array<int, 2>> dp(n);

    // 1. 마지막 집 제외: 0번 ~ n-2번
    dp[0][0] = 0;
    dp[0][1] = money[0];

    for (int i = 1; i <= n - 2; i++) {
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]);
        dp[i][1] = dp[i - 1][0] + money[i];
    }

    int answer1 = max(dp[n - 2][0], dp[n - 2][1]);

    // 2. 첫 집 제외: 1번 ~ n-1번
    dp[1][0] = 0;
    dp[1][1] = money[1];

    for (int i = 2; i < n; i++) {
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]);
        dp[i][1] = dp[i - 1][0] + money[i];
    }

    int answer2 = max(dp[n - 1][0], dp[n - 1][1]);

    return max(answer1, answer2);
}