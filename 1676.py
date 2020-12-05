n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
b.reverse()

l = []
if len(a) == 1 :
    for i in range(0, n) :
        l.append(a)
        if i == n-1 :
            break

        a = int(input())

    l[0] = int(l[0][0])
    b = sorted(l)
    b.reverse()
    for i in range(0, len(l)) :
        for j in range(0, len(b)) :
            if l[i] == b[j] :
                print(j+1)
                break

else :
    for i in range(0, len(a)) :
        for j in range(0, len(b)) :
            if a[i] == b[j] :
                print(j+1)
                break

