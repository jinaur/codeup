a, b = list(map(int, input().split()))

Max = 0
for i in range(a, b+1) :
    for j in range(a, b+1) :
        r = str(i*j)
        r2 = r[::-1]
        if int(r) > Max and r == r2 :
            Max = i*j

print(Max) 

