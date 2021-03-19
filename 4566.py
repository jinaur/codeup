n = int(input())
m = int(input())

l = []
for i in range(n, m+1) :
    for j in range(1, i+1) :
        if j != 1 and j != i and i%j == 0 :
            break
        else :
            if j != 1 and j == i :
                l.append(i)

print(sum(l))
print(min(l))

