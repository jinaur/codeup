n = int(input())

l = [1, 1]
for i in range(0, n-2) :
    l.append(l[i]+l[i+1])

print(l[len(l)-1])


