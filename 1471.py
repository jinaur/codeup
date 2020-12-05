n = int(input())

for i in range(0, n):
    for j in range(0, n):
        print(n-i + (i*n+1), end=" ")
    print()