n = int(input())

r = 0
l = [0] * 6
for i in range(0, n) :
    a = list(map(int, input().split()))
    for j in range(0, 6) :
        if a[j] > l[j] :
            l[j] = a[j]

r = 0
for i in range(0, len(l)) :
    r += l[i]

print(r)

