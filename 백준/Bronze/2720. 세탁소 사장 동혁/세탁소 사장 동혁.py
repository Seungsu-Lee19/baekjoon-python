import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    c = int(input())
    
    for i in range(4):
        if i == 0:
            print(f"{c // 25} ", end="")
            c = c - (25 * ( c // 25 ))
        elif i == 1:
            print(f"{c // 10} ", end="")
            c = c - (10 * ( c // 10 ))
        elif i == 2:
            print(f"{c // 5} ", end="")
            c = c - (5 * ( c // 5 ))
        elif i == 3:
            print(f"{c // 1} ", end="")
            c = c - (1 * ( c // 1 ))
    print()