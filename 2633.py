n, k = map(int, input().split())
a = list(map(int, input().split()))
r = n

for i in range(0, n-1) :
    if a[i] >= k :
        r = i
        break

print(r+1)

