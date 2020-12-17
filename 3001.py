n = int(input())
a = list(map(int, input().split()))
k = int(input())

r = -1
for i in range(0, n) :
    if a[i] == k :
        r += i + 2
        break

print(r)

