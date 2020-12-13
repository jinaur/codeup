a = list(map(int, input().split()))

r = 0
l = []
for i in range(0, len(a)) :
    l.append(a[i])
    r += a[i]

r = r/10
aa_count = 0
ba_count = 0

for i in range(0, len(a)) :
    if l[i] >= r :
        aa_count += 1
    else :
        ba_count += 1

print(r)
print(aa_count, ba_count)

