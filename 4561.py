l = []

for i in range(0, 7) :
    n = int(input())
    if n % 2 == 1 :
        l.append(n)

print(sum(l))
print(min(l))


