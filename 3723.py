n = int(input())
a = list(map(int, input().split()))

r = 0
count = 0
for i in range(0, n-2) :
    if count != 0 :
        count -=1
        continue

    if a[i] + a[i+1] > a[i+1] + a[i+2] :
        r += a[i] + a[i+1]
        count = 1
    elif a[i] + a[i+1] < a[i+1] + a[i+2] :
        r += a[i+1] + a[i+2]
        count = 2
    elif a[i+1] + a[i+2] < a[i+2] + a[i+3] :
        r += a[i+2] + a[i+3]
        count = 2

print(r)