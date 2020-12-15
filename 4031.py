a = list(map(int, input().split()))

r = 0
l1 = []
l2 = []

for i in range(0, 7) :
    if a[i] % 2 == 1 :
        l1.append(a[i])

for i in range(0, 7) :
    if a[i] % 2 == 0 :
        l2.append(a[i])

if len(l1) == 0 and len(l2) >= 1 :
    r += max(l2)
elif len(l2) == 0 and len(l1) >= 1 :
    r += max(l1)
else :
    r += max(l1) + max(l2)

print(r)


