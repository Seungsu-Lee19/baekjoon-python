N = int(input())
fruit = list(map(int, input().split()))

def calc():
    f = set(fruit)
    if len(f) <= 2:
        return N
    else:
        left = 0
        fruit_num = {}
        ans = 0
        for right in range(N):
            f = fruit[right]
            
            if f in fruit_num:
                fruit_num[f] += 1
            else:
                fruit_num[f] = 1
                
            while len(fruit_num) > 2:
                f = fruit[left]
                
                fruit_num[f] -= 1
                if fruit_num[f] == 0:
                    del fruit_num[f]
                    
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
    
print(calc())