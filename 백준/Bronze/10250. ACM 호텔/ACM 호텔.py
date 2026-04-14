T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())
    
    floor = n % h
    if floor == 0: floor = h
    ho = (n - 1) // h + 1
    print(f"{floor}{ho:02d}")