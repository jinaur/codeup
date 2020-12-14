n, s = list(map(int, (input().split())))
a = list(map(int, input().split()))

r = -1
for i in range(0, n) :
    if a[i] == s :
        r = i+1
        break

print(r)


