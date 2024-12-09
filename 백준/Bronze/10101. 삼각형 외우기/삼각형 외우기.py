import sys
import math
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print("Error")
elif a == 60 and b == 60 and c == 60:
    print("Equilateral")
elif a != b and b != c and c != a:
    print("Scalene")
else:
    print("Isosceles")
