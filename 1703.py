n = int(input())

h, m, s = 0, 0, 0

if n >= 3600 :
    for i in range(0, (n//3600)+1) :
        if n < 3600 :
            break
        h += 1
        n -= 3600
if n >= 60 :
    for i in range(0, (n//60)+1) :
        if n < 60 :
            break
        m += 1
        n -= 60

s = n
print(h, m, s)


