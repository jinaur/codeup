l = []

r = 0
for i in range(0, 10) :
    n = int(input())
    l.append(n)
    r += n

r = r // 10
print(r)
print(l[4])