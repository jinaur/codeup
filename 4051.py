count = 0

for i in range(0, 5) :
    a, b = list(map(float, input().split()))
    if b-a-1 >= 5 :
        count += 4
    elif b-a-1 <= 0 :
        continue
    else :
        count += b-a-1

m = count * 10000
if count >= 15 :
    m -= m*0.05
elif count <= 5 :
    m += m*0.05

print(int(m))
