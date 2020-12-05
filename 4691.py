n = int(input())

Max = 0
for i in range(0, n) :
    a, b, c, d = list(map(int, input().split()))
    if r >= Max :
        Max = r
    if a == b and b == c and c == d :
        r = 50000+a*10000
    elif a == b and b == c or 