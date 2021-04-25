n = int(input())

for i in range(0, n) :
    acount = [0]*4
    bcount = [0]*4
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for j in range(1, len(a)) :
        if a[j] == 4 :
            acount[3] += 1
        elif a[j] == 3 :
            acount[2] += 1
        elif a[j] == 2 :
            acount[1] += 1
        else :
            acount[0] += 1
    for j in range(1, len(b)) :
        if b[j] == 4 :
            bcount[3] += 1
        elif b[j] == 3 :
            bcount[2] += 1
        elif b[j] == 2 :
            bcount[1] += 1
        else :
            bcount[0] += 1

    if acount[3] > bcount[3] :
        print("A")
    elif acount[3] == bcount[3] and acount[2] > bcount[2] :
        print("A")
    elif acount[3] == bcount[3] and acount[2] == bcount[2] and acount[1] > bcount[1] :
        print("A")
    elif acount[3] == bcount[3] and acount[2] == bcount[2] and acount[1] == bcount[1] and acount[0] > bcount[0] :
        print("A")

    if acount[3] < bcount[3] :
        print("B")
    elif acount[3] == bcount[3] and acount[2] < bcount[2] :
        print("B")
    elif acount[3] == bcount[3] and acount[2] == bcount[2] and acount[1] < bcount[1] :
        print("B")
    elif acount[3] == bcount[3] and acount[2] == bcount[2] and acount[1] == bcount[1] and acount[0] < bcount[0] :
        print("B")
    if acount[3] == bcount[3] and acount[2] == bcount[2] and acount[1] == bcount[1] and acount[0] == bcount[0] :
        print("D")


