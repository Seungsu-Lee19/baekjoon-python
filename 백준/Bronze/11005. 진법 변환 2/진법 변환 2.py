import sys
input = sys.stdin.readline

num, jin = list(map(int,input().split()))

_int = 0

n = []
while True:
    a = num // jin
    b = num % jin
    
    if b < 10:
        n.append(b)
    else:
        n.append(chr(65 + b - 10))
    
    num = a
    
    if num <= 0:
        break
    

for i in n[::-1]:
    print(i, end="")
