n = int(input())
m = int(input())

l = []
for i in range(n, m+1) :
    r = True
    if i < 2 :
        r = False
    for j in range(2, i) :
        if i%j == 0 :
            r = False
    if r == True :
        l.append(i)
    
print(sum(l))
print(min(l))

