n = int(input())
l = []

for i in range(0, n) :
    a, b = map(int, input().split())
    l.append(a)
    l.append(b)

for j in range(0, n) :
    if a == j :
        print(l[j], l[j+1])    


