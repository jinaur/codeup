n = int(input())
a = list(map(int, input().split()))

l = []
for i in range(0, n) :
    l.append(a[i])

ll = sorted(l)

for i in range(0, n) :
    for j in range(0, n) :
        if l[i] == ll[j] :
            print(j, end=" ")

