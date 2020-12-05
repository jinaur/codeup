a, b = list(map(int, input().split()))

if a % 2 == 0 :
    a = (a//2) * 10
else :
    a = (a//2) + 1

if b % 2 == 0 :
    b = (b//2) * 10
else :
    b = (b//2) + 1

print(a+b)

