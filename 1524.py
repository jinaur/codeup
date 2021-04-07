l = []

for i in range(0, 9) :
    a = list(map(int, input().split()))
    l.append(a)

a, b = list(map(int, input().split()))
a, b = a-1, b-1
count = 0
# X X X
# O   X
# O O X
else :
    if l[a-1][b-1] == 1 :
        count += 1
    if l[a-1][b] == 1 :
        count += 1
    if l[a-1][b+1] == 1 :
        count += 1

    if l[a][b-1] == 1 :
        count += 1
    if l[a][b+1] == 1 :
        count += 1

    if l[a+1][b-1] == 1 :
        count += 1
    if l[a+1][b] == 1 :
        count += 1
    if l[a+1][b+1] == 1 :
        count += 1

if l[a][b] == 1 :
    print(-1)
else :
    print(count)

