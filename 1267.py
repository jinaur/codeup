n = int(input())
a = list(map(int, input().split()))

r = 0
for i in range(0, n) :
    if a[i] % 5 == 0 :
        r += a[i]

print(r)

