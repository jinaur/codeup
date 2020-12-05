a, b = list(map(int, input().split()))

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
r = len(str(a/b))
if r <= 3 :
    print(str(round(a/b, 2))+"0")
else :
    print(round(a/b, 2))

