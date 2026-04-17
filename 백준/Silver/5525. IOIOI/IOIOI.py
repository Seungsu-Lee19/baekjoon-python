N = int(input())
M = int(input())
S = input()
find_str = ''
for i in range(2*N + 1):
    if i % 2 == 0:
        find_str += 'I'
    else:
        find_str += 'O'

cnt = 0    
for i in range(M - (2 * N)):
    if S[i] == 'I':
        if S[i:i + 2*N + 1] == find_str:
            cnt += 1

print(cnt)