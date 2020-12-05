n = int(input())
a = list(map(int, input().split()))

print(a[0]+1, end=" ")
for i in range(1, n) :
    if a[0] > a[i] :
        print(a[i]+1, end=" ")
    else :
        print(a[i], end=" ")