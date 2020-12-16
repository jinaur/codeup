a, b = map(int, input().split())
l = []
l.append(a+b)
l.append(a-b)
l.append(a*b)
l.sort()

print(l[1])



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

# 밀도 = 질량 / 부피
# round(n, 3)
# M = 질량 Mass
# V = 부피 Volume
# R = 액체의 밀도

m, v, r = map(int, input().split())

a = m/v
a = round(a, 3)
if a > r :
    t = "DOWN"
elif a < r :
    t = "UP"
else :
    t = "STOP"

a = format(a, ".2f")

print(a, t)

