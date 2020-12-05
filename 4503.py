n = int(input())
k = int(input())

l = [1]
count = -1
for i in range(0, k) :
    a, b = list(map(int, input().split()))
    for j in range(0, len(l)) :
        if a == l[j] :
            l.append(b)
        if b == l[j] :
            l.append(a)

lcount = []
for i in range(0, n) :
    lcount.append(i+1)

for i in range(0, len(l)) :
    for j in range(0, len(lcount)) :
        if l[i] == lcount[j] :
            del lcount[j]
            count += 1

        
print(count)

