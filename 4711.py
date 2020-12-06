max = 0
r = 0

for i in range(0, 4) :
    a, b = map(int, input().split())
    r -= a
    r += b
    if r > max :
        max = r

print(max)
