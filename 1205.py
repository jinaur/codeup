a, b = list(map(int, input().split()))

Max = 0
if round(a+b) > Max :
    Max = round(a+b)
if round(a-b) > Max :
    Max = round(a-b, 6)
if round(b-a) > Max :
    Max = round(b-a, 6)
if round(a*b) > Max :
    Max = round(a*b, 6)
if round(a/b) > Max :
    Max = round(a/b, 6)
if round(b/a) > Max :
    Max = round(b/a, 6)
if round(a**b) > Max :
    Max = round(a**b, 6)

if round(b**a) > Max :
    Max = round(b**a, 6)

r = format(Max, ".6f")
print(r)

