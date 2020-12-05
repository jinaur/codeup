n = int(input())

for i in range(0, n):
    for j in range(0, n):
        print((i+1)*n-j, end=" ")
    print()