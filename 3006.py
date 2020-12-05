k = int(input())

for i in range(0, k) :
    n = int(input())
    for j in range(n-1, 1, -1) :
        if j*j == j**2 :
            print(j)
            break

