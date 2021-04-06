n = int(input())

for i in range(0, n) :
    for j in range(0, n) :
        if (i+1) % 2 == 1 :
            print(n*i+(j+1), end=" ")
        elif (i+1) % 2 == 0 :
            print(n*(i+1)-j, end=" ")
    print()

