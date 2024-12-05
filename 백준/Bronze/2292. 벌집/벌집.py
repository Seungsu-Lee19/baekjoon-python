import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print('1')
    exit()
elif n >= 2 and n <= 7:
    print("2")
    exit()
    
i = 1
start = 2
end = 7
while True:
    start = start + (i * 6)
    end = end + ((i + 1) * 6)
    i = i + 1
    
    if n >= start and n <= end:
        print(f"{i + 1}")
        break
    