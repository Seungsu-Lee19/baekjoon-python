a, p = map(int, input().split())
d = [a]

def dfs(v, visited, _p):
    # print(v, visited, _p)
    s = 0
    for i in str(v):
        s = s + int(int(i) ** _p)
    
    if s in visited:
        print(visited.index(s))
    else:
        visited.append(s)
        dfs(s, visited, _p)

dfs(a, d, p)