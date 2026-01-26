n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split())) # + - * //

_min = 1000000001
_max = -1000000001

def bfs(depth, cur):
    global _max, _min
    if depth == n - 1:
        _min = min(cur, _min)
        _max = max(cur, _max)
        
    if op[0] > 0:
        op[0] -= 1
        bfs(depth + 1, cur + a[depth + 1])
        op[0] += 1
        
    if op[1] > 0:
        op[1] -= 1
        bfs(depth + 1, cur - a[depth + 1])
        op[1] += 1
        
    if op[2] > 0:
        op[2] -= 1
        bfs(depth + 1, cur * a[depth + 1])
        op[2] += 1
        
    if op[3] > 0:
        op[3] -= 1
        bfs(depth + 1, int(cur / a[depth + 1]))
        op[3] += 1
        
bfs(0, a[0])
print(_max)
print(_min)