N, M = map(int, input().split())
tree = list(map(int, input().split()))

left = 0
right = max(tree)
ans = 0

def check(h, k):
    m = 0
    
    for t in tree:
        _m = t - h
        if _m > 0:
            m = m + _m
    
    return m >= k

while left <= right:
    mid = (left + right) // 2
    
    if check(mid, M):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
    
print(ans)
    