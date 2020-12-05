a, b, c = map(int, input().split())

Min = min(a, b, c)
Max = max(a, b, c)
l = [a, b, c]
l.remove(Max)
l.remove(Min)

if Max % Min == 0 and l[0] % Min == 0 :
    r = Min
else :
    for i in range(2, Max+1) :
        if Max % i == 0 and l[0] % i == 0 :
            r = i
            break

print(r)