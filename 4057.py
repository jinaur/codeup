a, b = list(map(int, input().split()))

Min = 1000000
Max = 0
r = 0

for i in range(a, b+1) :
    for j in range(2, i) :
        if i%j == 0 :
            continue
        else :
            r += 1
            if i > Max :
                Max = i
            if i < Min :
                Min = i

print(r)
print(Max+Min)

