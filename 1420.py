n = int(input())

ln = []
l = []
for i in range(0, n) :
    a, b = input().split()
    ln.append(a)
    l.append(int(b))

ll = sorted(l)
ll.reverse()

for i in range(0, n) :
    if ll[2] == l[i] :
        print(ln[i])


