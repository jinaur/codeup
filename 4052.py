a = input().split()

Max = 0
Min = 10000000000000000000000000000000
for i in range(0, len(a)) :
    r = 0
    for j in range(0, len(a[i])) :
        r += int(a[i][j])

    if r > Max :
        Max = r
    if r < Min :
        Min = r

print(Max, Min)

