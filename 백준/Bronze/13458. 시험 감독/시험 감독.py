n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

num = 0
for i in range(n):
    num += 1 # 총 감독
    a[i] = a[i] - b
    
    if a[i] > 0:
        if a[i] % c > 0:
            num = num + a[i] // c + 1
        else:
            num = num + a[i] // c
print(num)
