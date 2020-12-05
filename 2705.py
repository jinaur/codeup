n = int(input())
l, t = list(map(int, input().split()))
a = list(map(int, input().split()))

r = 0
count = 0
i_count = 0
for i in range(0, n) :
    if a[i] < i_count + count :
        continue
    else :
        count = 0

    for j in range(1, l+1) :
        if i >= n-j :
            break
        if a[i] == a[i+j] :
            i_count = a[i]
            count += t
            break

    if count == 0 :
        r += 10000

print(r)