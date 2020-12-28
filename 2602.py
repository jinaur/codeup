l = []
l1 = []
l2 = []
l3 = []

for i in range(0, 3) :
    a = list(map(int, input().split()))
    r = 0
    for j in range(0, 3) :
        r += a[j]
        print(a[j], end=" ")
    print(r)
    l1.append(a[0])
    l2.append(a[1])
    l3.append(a[2])
    l.append(r)

print(sum(l1), sum(l2), sum(l3), sum(l))

