n = int(input())

for i in range(0, n) :
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    la = []
    lb = []
    for j in range(0, a[0]) :
        la.append(a[i+1])
    for k in range(0, b[0]) :
        lb.append(b[i+1])

    la.sort()
    lb.sort()
    la.reverse()
    lb.reverse()
    acount = 0
    bcount = 0
    for r in range(0, n) :
        for x in range(1, r+1) :
            if la[x] == x :
                acount += 1
            elif lb[x] == x :
                bcount += 1

        if acount == bcount :
            print("D")
        elif acount > bcount :
            print("A")
        elif acount < bcount :
            print("B")
            
    