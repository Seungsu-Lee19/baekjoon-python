n = int(input())

dp = [[0 for _ in range(2)] for _ in range(n + 1)]
stair = [0]
for _ in range(n):
    stair.append(int(input()))

def dynamic():
    dp[1][0] = stair[1]

    dp[2][0] = stair[1] + stair[2]
    dp[2][1] = stair[2]

    for i in range(3, n + 1):
        dp[i][0] = dp[i - 1][1] + stair[i]
        dp[i][1] = max(dp[i - 2][0] + stair[i], dp[i - 2][1] + stair[i])

if n == 1:
    print(stair[1])
elif n == 2:
    print(stair[1] + stair[2])
else:
    dynamic()
    print(max(dp[-1]))

