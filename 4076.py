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


