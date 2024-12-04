import sys
input = sys.stdin.readline

sum = 0
cnt = 0
for i in range(20):
    a, b, c = input().split()
    
    if c != 'P':
        sum += float(b)
    if c != 'P' and c != 'F':
        grade = ord('E') - ord(c[0])
        if c[1] == '+':
            grade += 0.5
        cnt += grade * float(b)

if sum == 0:
    print("0.000000")
else:
    print(f'{cnt / sum:.6f}')
