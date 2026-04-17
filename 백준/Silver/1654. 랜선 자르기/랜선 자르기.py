K, N = map(int, input().split())

lan = []
for _ in range(K):
    lan.append(int(input()))

lan.sort()
left = 0
right = lan[-1]
ans = 0

def check(l, k):
    cnt = 0
    for i in lan:
        cnt = cnt + (i // l)

    return cnt >= k

while left <= right:
    mid = (left + right) // 2
    
    if mid == 0:
        ans = 1
        break
    
    if check(mid, N):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)