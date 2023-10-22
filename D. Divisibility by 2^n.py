import math

M = 998244353

def mod(x):
    return ((x % M + M) % M)

def add(a, b):
    return mod(mod(a) + mod(b))

def mul(a, b):
    return mod(mod(a) * mod(b))

def get_count(x):
    total = 0
    while x % 2 == 0:
        x //= 2
        total += 1
    return total

def solve():
    n = int(input())
    x = 0
    extra = 0
    a = list(map(int, input().split()))
    b = []
    
    for i in range(n):
        x += get_count(a[i])
        cnt = get_count(i + 1)
        extra += cnt
        b.append(cnt)
    
    if x >= n:
        print(0)
        return
    
    if x + extra < n:
        print(-1)
        return
    
    ans = 0
    b.sort(reverse=True)
    
    for i in b:
        ans += 1
        if x + i >= n:
            break
        x += i
    
    print(ans)

if __name__ == "__main__":
    t = 1
    t = int(input())
    
    for i in range(1, t + 1):
        solve()
