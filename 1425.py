n, c = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort()

for i in range(0, n) :
    if (i)%c == 0 :
        print()
    print(a[i], end=" ")

