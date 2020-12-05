a = list(map(int, input().split()))

r = 100
for i in range(0, len(a)) :
    for j in range(0, 10) :
        if a[j] >= r :
            print("#", end=" ")
        else :
            print(" ", end=" ")
    r -= 10
    print(" ")

