n = list(input())

# 숫자에 0이 없으면 -1
# 0을 제외하고 각 자리의 합이 3으로 나눠떨어지지 않으면 -1
# 위 두 조건을 만족하면 내림차순 정렬

li = [s for s in n]

if '0' not in li:
    print(-1)
else:
    _sum = 0
    li.sort(reverse=True)
    for i in li:
        _sum += int(i)
    if _sum % 3 != 0:
        print(-1)
    else:
        print(''.join(li))
        