n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

Max = -10000000000000
for i in range(0, n) :
    r = 0
    try :
        for j in range(0, k) :
            r += a[i+j]
        if r > Max :
            Max = r
    except IndexError :
        break

print(Max)

