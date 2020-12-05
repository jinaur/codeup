n = int(input())
l = []

for i in range(0, n) :
    l.append([0]*n)

i, j = n//2, 0
k = 1

while True :
    if l[j][i] != 0 :
        break
    l[j][i] = k
    if k%n == 0 :
        j += 1 
        if j > n-1 :
            j = 0
    else :
        j -= 1 
        i += 1
        if j < 0 :
            j = n-1
        if i > n-1 :
            i = 0
    k += 1

for j in range(0, n) :
    for i in range(0, n) :
        print(l[j][i], end=" ")
    print()