import sys
input = sys.stdin.readline

num, jin = input().split()

_int = 0
jin = int(jin)

for i in range(len(num)):
    dec = ord(num[::-1][i])
    
    if dec >= 48 and dec <= 57:
        dec = dec - 48
    elif dec >= 65 and dec <= 90:
        dec = dec - 65 + 10
    
    
    _int += dec * (jin ** i)

print(_int)