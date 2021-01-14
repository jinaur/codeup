l = []*5

for i in range(0, 5) :
    a = list(map(int, input().split()))
    l.append(a)

Max = 0
for i in range(1, 4) :
    for j in range(1, 4) :
        count = 0 
        count += l[i][j]
        count += l[i-1][j] 
        count += l[i+1][j]
        count += l[i][j-1]
        count += l[i][j+1]
        count += l[i-1][j-1]
        count += l[i-1][j+1]
        count += l[i+1][j-1]
        count += l[i+1][j+1]
        if count > Max :
            Max = count

print(Max)



