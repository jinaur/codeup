n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort()
r = 0
count = int((k-1)*(k//2))

for i in range(0, k) :
    r += a[len(a)-i-1]

print(r-count)

