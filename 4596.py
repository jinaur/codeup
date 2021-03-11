l = []

for i in range(0, 9) :
    l.append([])
for i in range(0, 9) :
    a = list(map(int, input().split()))
    for j in range(0, 9) :
        l[i].append(a[j])

Max = 0
r = [0, 0]
for i in range(0, 9):
    for j in range(0, 9) :
        if l[i][j] > Max :
            Max = l[i][j]
            r[0] = i+1
            r[1] = j+1

print(Max)
print(r[0], r[1])

