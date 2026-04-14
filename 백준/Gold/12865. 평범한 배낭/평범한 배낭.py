N, K = map(int, input().split())

items = []
dp = [0 for _ in range(K + 1)]
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

items.sort()
used_items = [[] for _ in range(K + 1)]
    
for i in range(1, K + 1):
    max_dp = 0
    used_j = 0
    w = 0
    v = 0
    
    for _w, _v in items:
        if _w > i:
            break
        
        j = i - _w
        
        if (_w, _v) not in used_items[j]:
            if max_dp < dp[j] + _v:
                max_dp = dp[j] + _v
                used_j = j
                w = _w
                v = _v
                    
    dp[i] = dp[used_j] + v
    used_items[i] = used_items[used_j] + [(w, v)]

print(max(dp))