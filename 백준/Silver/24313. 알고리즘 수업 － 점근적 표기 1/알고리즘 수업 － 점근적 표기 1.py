import sys
input = sys.stdin.readline

a, b = list(map(int, input().split()))
c = int(input())
n = int(input())

if (c - a) < 0:
    print('0')
elif (c - a) == 0:
    if b < 0:
        print('1')
    else:
        print("0") 
elif b / (c - a) <= n:
    print("1")
else:
    print("0")
            