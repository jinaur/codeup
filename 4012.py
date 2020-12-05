n = int(input())
a = list(map(int, input().split()))

l = a
la = sorted(l)
print(la)
for i in range(0, n) :
    for j in range(0, n-1) :
        if l[i] == la[j] and l[i] == la[j]+1 :
            print(l[i], j+1)
            break