a, b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

l = []
for i in range(0, a) :
    l.append(c[i])
for i in range(0, b) :
    l.append(d[i])

l.sort()
for i in range(0, len(l)) :
    print(l[i], end=" ")

