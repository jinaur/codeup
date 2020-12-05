n = int(input())

for k in range(0, n) :
    for t in range(0, n) :
        if (n-k) == t**2 :
            print(k, t)
            exit()

