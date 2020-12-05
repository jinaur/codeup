n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for i in range(0, m) :
    for j in range(0, n) :
        if a[j] == b[i] :
            print(j+1, end=" ")
            break
        if j+1 == m and a not in b :
            print(-1, end=" ")
            break