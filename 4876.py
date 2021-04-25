n = int(input())

for i in range(0, n) :
    acount4 = 0
    acount3 = 0
    acount2 = 0
    acount1 = 0

    bcount4 = 0
    bcount3 = 0
    bcount2 = 0
    bcount1 = 0
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for j in range(1, len(a)) :
        if a[j] == 4 :
            acount4 += 1
        elif a[j] == 3 :
            acount3 += 1
        elif a[j] == 2 :
            acount2 += 1
        else :
            acount1 += 1

    for j in range(1, len(b)) :
        if b[j] == 4 :
            bcount4 += 1
        elif b[j] == 3 :
            bcount3 += 1
        elif b[j] == 2 :
            bcount2 += 1
        else :
            bcount1 += 1

    if acount4 > bcount4 :
        print("A")
        continue
    elif acount4 == bcount4 and acount3 > bcount3 :
        print("A")
        continue
    elif acount4 == bcount4 and acount3 == bcount3 and acount2 > bcount2 :
        print("A")
        continue
    elif acount4 == bcount4 and acount3 == bcount3 and acount2 == bcount2 and acount1 > bcount1 :
        print("A")
        continue

    if acount4 < bcount4 :
        print("B")
        continue
    elif acount4 == bcount4 and acount3 < bcount3 :
        print("B")
        continue
    elif acount4 == bcount4 and acount3 == bcount3 and acount2 < bcount2 :
        print("B")
        continue
    elif acount4 == bcount4 and acount3 == bcount3 and acount2 == bcount2 and acount1 < bcount1 :
        print("B")
        continue
    
    if acount4 == bcount4 and acount3 == bcount3 and acount2 == bcount2 and acount1 == bcount1 :
        print("D")


