n, k = map(int, input().split())
l = []

for i in range(1, n+1) :
    if n%i == 0 :
        l.append(i)

try :
    print(l[k-1])
except IndexError :
    print(0)


