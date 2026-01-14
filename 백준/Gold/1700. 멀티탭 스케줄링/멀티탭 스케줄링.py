n, k = map(int, input().split())
a = list(map(int, input().split()))

pluged = []
result = 0

# 플러그에 안꼽혀있으면 꼽고 사용 횟수 마이너스
# 이미 꼽혀있다면 사용 횟수 마이너스
# 플러그가 꽉차면 가장 먼거리에 있는 번호 뽑기 => 이때 result += 1

while len(a) > 0:
    if len(pluged) < n and a[0] not in pluged:
        pluged.append(a[0])
        a.remove(a[0])
    elif len(pluged) < n and a[0] in pluged:
        a.remove(a[0])
    elif len(pluged) == n and a[0] in pluged:
        a.remove(a[0])
    elif len(pluged) == n and a[0] not in pluged:
        _max = -1
        for i in range(len(pluged)):
            if pluged[i] not in a:
                pluged.remove(pluged[i])
                result += 1
                break
            else:
                idx = a.index(pluged[i])
                if idx > _max:
                    _max = idx
        if len(pluged) < n:
            continue
        elif _max > -1:
            pluged.remove(a[_max])
            result += 1

print(result)

