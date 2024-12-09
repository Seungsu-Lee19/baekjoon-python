import sys
import math
input = sys.stdin.readline

a = int(input())

if a == 1:
    exit()


prime_number = 2
while True:
    _int = 2
    temp = 1
    for i in range(2, _int):
        if prime_number % i == 0:
            temp = 0
            break
    _int += 1
    
    if temp == 1:
        while True:
            if a % prime_number == 0:
                print(f"{prime_number}")
                a = a / prime_number
            else:
                break
    prime_number += 1

    if prime_number > a:
        break

