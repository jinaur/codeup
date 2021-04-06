n = int(input())

for i in range(0, n) :
    for j in range(0, n) :
        if j % 2 == 0 :
            print(i+1+(j*n), end=" ")
        elif j % 2 == 1 :
            print(i+1+(j*n)-j, end=" ")
    print()