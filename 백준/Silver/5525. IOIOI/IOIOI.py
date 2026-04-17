N = int(input())
M = int(input())
S = input()

cnt = 0
cur = 0
i = 1

while i < M - 1:
    if S[i - 1] == 'I' and S[i] == 'O' and S[i + 1] == 'I':
        cur += 1
        
        if cur >= N:
            cnt += 1
        
        i += 2
    else:
        cur = 0
        i += 1

print(cnt)