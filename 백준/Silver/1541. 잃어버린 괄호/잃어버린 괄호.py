import re

s = input()

tokens = re.split(r'([+-])', s)

# -부호가 나오면 괄호 열고, 다음 부호가 -이면 괄호 닫기.
# 0 2 4 6 ... => 숫자
# 1 3 5 7 ... => 부호
# 즉, 마이너스 부호가 있다면 그 뒤에 숫자는 다 빼버리면 됨.

_sum = 0

if '-' in tokens:
    idx = tokens.index('-')
    for i in range(0, len(tokens), 2):
        if i > idx:
            _sum -= int(tokens[i])
        elif i < idx:
            _sum += int(tokens[i])
else:
    for i in range(0, len(tokens), 2):
        _sum += int(tokens[i])

print(_sum)
