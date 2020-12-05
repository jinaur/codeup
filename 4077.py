# a = 미세먼지 농도
# b = 초미세먼지 농도
# c = 오존 농도 
# 미세먼지 Blue = 0~30, Green = 31~80, Yellow = 81~150, Red 151이상
# 초미세먼지 Blue = 0~15, Green = 16~35, Yellow = 36~75, Red 76이상
# 오존 Blue = 0~30, Green = 31~90, Yellow = 91 ~ 150, Red 151이상
# Blue = 야회 활동 권장
# Green = 야외 활동 가능
# Yellow = 야외 활동 자제
# Red = 야외 활동 금지

a, b, c = list(map(int, input().split()))

a_density = ""
b_density = ""
c_density = ""
max_density = ""

if a >= 151  or b >= 76 or c >= 151 :
    max_density = "Stop"

if a >= 151  or b >= 76 or c >= 151 :
    max_density = "Stop"
    
if a >= 151  or b >= 76 or c >= 151 :
    max_density = "Stop"

if a >= 151 :
    a_density = "Red"
elif a <= 150 and a >= 81 :
    a_density = "Yellow"
elif a <= 80 and a >= 31 :
    a_density = "Green"
else :
    a_density = "Blue"

if b >= 76 :
    b_density = "Red"
elif b <= 75 and b >= 36 :
    b_density = "Yellow"
elif b <= 35 and b >= 16 :
    b_density = "Green"
else :
    b_density = "Blue"

if c >= 151 :
    c_density = "Red"
elif c <= 150 and c >= 91 :
    c_density = "Yellow"
elif c <= 90 and c >= 31 :
    c_density = "Green"
else :
    c_density = "Blue"

print(a, a_density)
print(b, b_density)
print(c, c_density)
