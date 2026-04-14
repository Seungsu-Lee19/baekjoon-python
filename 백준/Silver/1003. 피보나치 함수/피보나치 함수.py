T = int(input())

dp = [[] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 41):
    x = dp[i - 1][0] + dp[i - 2][0]
    y = dp[i - 1][1] + dp[i - 2][1]
    dp[i] = [x, y]

for _ in range(T):
    n = int(input())
    
    print(*dp[n])
    