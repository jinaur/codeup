from collections import Counter

l = []

r = 0
for i in range(0, 10) :
    n = int(input())
    l.append(n)
    r += n

c = Counter(l)
r = r // 10
print(r)
print(c.most_common(1)[0][0])

