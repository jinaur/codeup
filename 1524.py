l = [[], [], [], [], [], [], [], [], []]

for i in range(0, 9) :
    a = list(map(int, input().split()))
    for j in range(0, 9) :
        l[i].append(a[j])

a, b = list(map(int, input().split()))

count = 0
if l[a-1][b-1] == 1 :
    print(-1)
    exit()

if l[a-2][b-1] == 1 :
    count += 1
if l[a][b-1] == 1 :
    count += 1
if l[a-1][b] == 1 :
    count += 1
if l[a][b-2] == 1 :
    count += 1
if l[a-2][b-2] == 1 :
    count += 1
if l[a-2][b] == 1 :
    count += 1
if l[a][b-2] == 1 :
    count += 1
if l[a][b] == 1 :
    count += 1

print(count)

