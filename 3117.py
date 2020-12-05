n = int(input())

l = []
for i in range(0, n) :
    a = int(input())
    if a == 0 :
        del l[len(l)-1]
    else :
        l.append(a)

print(sum(l))

