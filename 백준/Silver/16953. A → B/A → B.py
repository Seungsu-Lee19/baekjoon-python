a, b = input().split()

cnt = 1

# 마지막 숫자가 1이면 2로 나눠지지 않기 때문에 1을 빼고
# 1이 아니면 2로 나눔
# 근데 소수점이 생긴다? -1
# 아니면 계속 진행

while True:
    if b[-1] == '1':
        b = b[:-1]
        cnt += 1
    else:
        temp = int(b) / 2
        if (temp - int(temp)) > 0:
            print(-1)
            break
        
        b = str(int(temp))
        cnt += 1
        
    if a == b:
        print(cnt)
        break
    elif int(a) > int(b):
        print(-1)
        break
    