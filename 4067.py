n, m = list(map(int, input().split()))

l = []
for i in range(0, n) :
    r = 0
    a, b, c = list(map(int, input().split()))
    r += a*2
    r += b
    l.append(r)

la = sorted(l)
la.reverse()
for i in range(0, len(l)) :
    if l[m-1] == la[i] and i == m :
        print(i+1)
        break

