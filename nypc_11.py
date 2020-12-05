n = int(input())

l = []
for i in range(0, n) :
    a, b, c = list(map(int, input().split(":")))
    r = c
    for j in range(0, 99) :
            if a > 0 :
                a -= 1
                r += 60000
            if b > 0 :
                b -= 1
                r += 1000

            if a == 0 and b == 0 :
                break
    
    l.append(r)

if n % 2 != 0 :
    l.remove(max(l))

# 1초는 1000
# 10초는 10000
# 60초는 60000

Min = l[0]+l[1]
x = 0

for i in range(2, n-2) :
    if l[i]+l[i+1] < Min :
        Min = l[i]+l[i+1]

for i in range(0, n-2, 2) :
    if abs(l[i]+l[i+1]-Min) < 10000 :
        x += 1

print(x)
       