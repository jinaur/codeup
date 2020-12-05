n = int(input())
k = int(input())
a = list(map(int, input().split()))

count = 0
a.reverse()
for i in range(0, k) :
    if n % a[i] == 0 :
        n -= a[i] * 2
        count += 2
        break
    elif n % a[i] == 0 :
        n -= a[i] * 3
        count += 3
        break
    if a[i]*2 >= a[0] and a[i]*2 <= n :
        n -= a[i+1] * 2
        count += 2
        break

while True :
    for i in range(0, k) :
        if n <= 0 :
            print(count)
            exit()
        if a[i] <= n :
            n -= a[i]
            count += 1
            break
        