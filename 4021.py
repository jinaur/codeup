a = list(map(int, input().split()))

r = 0

for i in range(0, len(a)) :
    if a[i] % 2 == 1 :
        r += a[i]
    
if r == 0 :
    print(-1)
else :
    print(r)

