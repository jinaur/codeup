a, b, c = list(map(int, input().split()))

if a <= 170 :
    print("CRASH", a)
elif b <= 170 :
    print("CRASH", b)
elif c <= 170 :
    print("CRASH", c)
else :
    print("PASS")