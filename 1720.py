n = int(input())

count = 0
for i in range(0, n) :
    a = list(map(int, input().split()))
    r = a[3]
    del a[3]
    if min(a) == r :
        continue
    else :
        count = 1
        print(i+1, min(a))

if count == 0 :
    print(-1)

