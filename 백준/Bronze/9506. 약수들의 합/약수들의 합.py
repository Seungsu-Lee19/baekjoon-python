import sys
import math
input = sys.stdin.readline

while True:
    a = int(input())

    if a == -1:
        break
    
    _int = 1
    c = []
    while True:
        if a % _int == 0:
            c.append(_int)

        _int += 1

        if a <= _int:
            break
    
    if sum(c) == a:
        print(f"{a} = ", end="")
        print(*c, sep=' + ')
    else:
        print(f"{a} is NOT perfect.")
    


