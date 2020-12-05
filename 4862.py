n = int(input())

Max = 0
for i in range(0, n) :
    a, b, c = list(map(int, input().split()))
    if a == b and b == c :
        r = 10000+a*1000
    elif a == b or a == c  :
        r = 1000+a*100
    elif b == c :
        r = 1000+b*100
    else :
        r = max(a, b, c) * 100

    if r > Max :
        Max = r 

print(Max)