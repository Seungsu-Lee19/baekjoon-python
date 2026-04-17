N = int(input())
M = int(input())
S = input()
# find_str = ''
# for i in range(2*N + 1):
#     if i % 2 == 0:
#         find_str += 'I'
#     else:
#         find_str += 'O'

cnt = 0
i = 0   
while i < M - (2 * N):
    if S[i] == 'I':
        good = True
        for j in range(i, i + 2*N + 1):
            find_s = None
            if (j - i) % 2 == 0:
                find_s = 'I'
            else:
                find_s = 'O'
            
            if find_s != S[j]:
                good = False
                break
        
        if good:
            cnt += 1
            i = i + 2
            continue
        
    i += 1
                
print(cnt)