N = int(input())

dp = [int(1e9) for _ in range(N + 1)]
dp[N] = 0
for i in range(N - 1, 0, -1):
    min_dp = dp[i]
    if i * 2 <= N:
        min_dp = min(min_dp, dp[i * 2] + 1)
    if i * 3 <= N:
        min_dp = min(min_dp, dp[i * 3] + 1)
    if i + 1 <= N:
        min_dp = min(min_dp, dp[i + 1] + 1)
    dp[i] = min_dp

print(dp[1])

    