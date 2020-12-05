n = int(input())

l = []
# l_len = []
# Min = 1000
for i in range(0, n) :
    a = input()
    # l_len.append(len(a))
    for j in range(0, len(a)) :
        # if ord(a[j]) < Min :
            # l.append(ord(a[j]))
        l.append(ord(a[j]))

l.sort()

for i in range(0, len(l)) :
    if i % len(a) == 0 and i != 0 :
        print()
    
    print(chr(l[i]), end="")
    


