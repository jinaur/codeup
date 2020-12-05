n, m = map(int, input().split())

l1 = []

for i in range(0, n) :
    s, y = map(int, input().split())
    if y == 1 or y == 2 :
        l1.append(s)
    if len(l1) >= m :
    