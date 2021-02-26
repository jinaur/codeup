n = int(input())

Max = 0
r = 0
for i in range(0, n) :
    a, b, c, d = list(map(int, input().split()))
    if r >= Max :
        Max = r
    if a == b and b == c and c == d :
        r = 50000+a*10000
    elif a == b and a == c :
        r = 10000+a*1000
    elif a == c and a == d :
        r = 10000+a*1000
    elif b == c and b == d :
        r = 10000+a*1000