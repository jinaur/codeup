n, m = map(int, input().split())

for i in range(0, n):
    for j in range(0, m):
        print((n-i)*m-j, end=" ")
    print()

    