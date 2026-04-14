num = list(map(int, input().split()))

s = 0
for n in num:
    s = s + (n * n)
print(s % 10)