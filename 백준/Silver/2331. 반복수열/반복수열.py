a, p = map(int, input().split())
d = [a]

s = a
while True:
    _s = 0
    for i in str(s):
        _s = _s + int(int(i) ** p)
    
    if _s in d:
        print(d.index(_s))
        break
    
    d.append(_s)
    s = str(_s)
