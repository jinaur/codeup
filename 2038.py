a = list(map(int, input().split()))
b = int(input())
c = input().split()
d, r = list(map(int, input().split()))
h = sum(a)
k = str(b)
kk = int(k)
count = 0

if c[0] == "1" and len(c) == 3 :
    if len(c) == 3 :
        c[1] = k+c[1]
        count = int(c[2])
        k = eval(c[1])
    else :
        c[1] = k+c[1]+c[2]
        count = int(c[3])  
for i in range(0, h) :
    if count >= 1 :
        r -= int(k)
        count -= 1
    else :
        r -= kk

    if r <= 0 :
        print(1)
        break
    h -= d
    if h <= 0 :
        print(0)
        break
    
