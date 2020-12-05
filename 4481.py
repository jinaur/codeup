l1 = []
l2 = []

for i in range(0, 5) :
    a, b = input().split()
    l1.append(a)
    l2.append(int(b))

l2.sort()
l1_a = l1
l1_a.reverse()

for i in range(0, 4) :
    if l2[i] >= l2[i+1] :
        count += 1
    else :
        break
    
for i in range(0, 5) :
    if l1 == l1_a and :
