n, m = map(int, input().split())

for i in range(0, n):
    for j in range(0, m):
        print((n-i-1)*m+(j+1), end=" ")
    print()
