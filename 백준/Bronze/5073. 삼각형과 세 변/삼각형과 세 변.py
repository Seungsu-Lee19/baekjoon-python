import sys
input = sys.stdin.readline


while True:
    a, b, c = list(map(int, input().split()))


    if a == 0 and b == 0 and c == 0:
        break
    elif 2 * max([a, b, c]) >= sum([a, b, c]):
        print("Invalid")
    elif a == b and b == c and c == a:
        print("Equilateral")
    elif a == b and a != c and b != c:
        print("Isosceles")
    elif a == c and a != b and c != b:
        print("Isosceles")
    elif b == c and b != a and c != a:
        print("Isosceles")
    else:
        print("Scalene")

