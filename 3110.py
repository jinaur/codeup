n, k = list(map(int, input().split()))

l = []
for i in range(1, n+1) :
    l.append(i)


for i in range(0, n) :
    if i*k >= n :
        i = 0
    del l[i*k]
    print(l)