n, k = map(int, input().split())

money = []
for _ in range(n):
    money.append(int(input()))

coin = 0
for i in range(n-1, -1, -1):
    if k // money[i] > 0:
        coin = coin + (k // money[i])
        k = k - (k // money[i]) * money[i]
        
    
print(coin)