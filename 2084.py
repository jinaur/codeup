n = int(input())
a = list(map(int, input().split()))
m = int(input())

for i in range(0, m) :
    count = 0
    s = int(input())
    for j in range(0, n) :
        if a[j] == s :
            count = 1
            print(j+1)
            break
    if count == 0 :
        print(-1)


 