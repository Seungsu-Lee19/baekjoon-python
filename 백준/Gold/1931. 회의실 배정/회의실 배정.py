n = int(input())
meeting = []

for _ in range(n):
    a, b = map(int, input().split())
    meeting.append([a, b])
    
meeting.sort()

# 가장 빨리 시작하는 순으로 정렬
# 가장 빠른 회의 시작
# 만약 뒤에 더 짧은 회의가 있다? 변경
# 이후에는 반복

flag = meeting[0]
cnt = 1
for i in range(1, len(meeting)):
    # print(flag, meeting[i], cnt)
    if flag[0] == meeting[i][0] and flag[1] == meeting[i][1] and flag[1] <= meeting[i][0]:
        cnt += 1
    elif flag[1] <= meeting[i][0]:
        flag = meeting[i]
        cnt += 1
    elif flag[0] < meeting[i][0] and flag[1] >= meeting[i][1]:
        flag = meeting[i]
    elif flag[0] <= meeting[i][0] and flag[1] > meeting[i][1]:
        flag = meeting[i]
    
print(cnt)
