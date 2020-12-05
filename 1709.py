n = int(input())
a = list(map(int, input().split()))

l = []
for i in range(0, n) :
    l.append(a[i])

l.sort()
l.reverse()
for i in range(0, len(l)) :
    print(l[i], end=" ")

