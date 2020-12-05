count = 0
r = 0
e = 0

for i in range(0, 5):
    a, b = map(float, input().split())
    if b - a >= 4 :
        count += 4
    else :
        count += b - a

count -= 5
if count <= 5 :
    e = True
elif count >= 15 :
    e = 1

for i in range(0, int(count*2)) :
    if count >= 0.5 :
        count -= 0.5
        r += 5000

if e == True :
    r += r * 0.05
elif e == 1 :
    r -= r * 0.05

print(int(r))