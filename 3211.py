n, m = list(map(int, input().split()))
l = list(map(int, input().split()))

for i in range(0, m) :
    a, b = list(map(int, input().split()))
    Max = 0
    Min = 1000000000
    for i in range(a-1, b) :
        if l[i] > Max :
            Max = l[i]
        if l[i] < Min :
            Min = l[i]

    print(Max - Min)
    