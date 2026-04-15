N, M = map(int, input().split())
num = [0] + list(map(int, input().split()))
dp = [0]
for i in range(1, N + 1):
    dp.append(dp[i - 1] + num[i])

for _ in range(M):
    i, j = map(int, input().split())
    
    print(dp[j] - dp[i - 1])
    
