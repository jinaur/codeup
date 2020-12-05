n = int(input())

for i in range(1, n+1) :
    r = 0 
    a, b, = list(map(int, input().split()))
    for j in range(a, (b//2)) :
        r += j
    for k in range(b//2, b+1) :
        r += k

    print("Scenario", "#" + str(i) + ":")
    print(r)
    print()

