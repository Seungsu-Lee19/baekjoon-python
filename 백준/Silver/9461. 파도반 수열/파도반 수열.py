T = int(input())

def dynamic(n):
    dp = [0 for _ in range(101)]
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    
    for i in range(6, n + 1):
        dp[i] = dp[i - 1] + dp[i - 5]

    return dp[n]

for _ in range(T):
    n = int(input())
    
    print(dynamic(n))