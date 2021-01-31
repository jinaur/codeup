Max = 0
Max_2 = 0

l = []
for i in range(0, 7) :
    n = int(input())
    l.append(n)

l.sort()
l.reverse()

for i in range(0, len(l)) :
    if l[i] > Max :
        Max = l[i]
    elif l[i] > Max_2 and l[i] <= Max :
        Max_2 = l[i]

print(Max)
print(Max_2)

