a = list(map(int, input().split()))

for i in range(0, 5) :
    count = 0
    for j in range(1, a[i]) :
        if a[i] % j == 0 :
            count += j

    if count == a[i] :
        print("yes")
    else :
        print("no")

