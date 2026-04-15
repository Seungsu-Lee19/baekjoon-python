N = int(input())

dp = [int(1e9) for _ in range(N + 1)]
dp[0] = 0

for i in range(1, N + 1):
    min_dp = int(1e9)
    for j in range(1, i + 1):
        k = i - (j * j)
        
        if k < 0:
            break
        
        min_dp = min(min_dp, dp[k] + 1)
    dp[i] = min_dp
    
print(dp[N])