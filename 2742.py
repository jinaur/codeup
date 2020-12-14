a = list(map(int, input().split()))
n = a[0]
a.sort()
a.reverse()
a.remove(n)
r = max(a)

a[0] = a[n//2]
a[n//2] = r

for i in range(0, n) :
    print(a[i], end=" ")


