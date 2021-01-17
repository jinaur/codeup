a = list(map(int, input().split()))

count = 0
l = [0, 0]

for i in range(0, len(a)) :
    if len(l) >= 3 :
        del l[0]

    if a[i] == l[0] or a[i] == l[1] :
        count += 1

    if a[i] != l[1] : 
        l.append(a[i])    

print(count)



