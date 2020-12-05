a, b = map(int, input().split())

m = 0
count = 0
r = 0

for i in range(0, a) :
    if r >= a :
        break
    
    r += 1
    m += 1
    count += 1

    if m >= b :
        m -= b
        r += 1

print(count)
