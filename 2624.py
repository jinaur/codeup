n = int(input())

l = []
if n < 2 :
    print(1)
    exit()

for i in range(2, n+1) :
    r = True
    for j in range(2, i) :
        if i%j == 0 :
            r = False

    if r == True :
        l.append(i)

print(sum(l))