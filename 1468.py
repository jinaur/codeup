n = int(input())

for i in range(0, n) :
    for j in range(0, n) :
        print(n-j + (n*i)[::-1], end=" ")
    print()
