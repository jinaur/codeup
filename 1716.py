a, b = list(map(int, input().split()))

r = 0
for i in range(a, 11) :
    if i % 2 == 0 :
        r += 30 - b
        b = 0 
    elif i % 2 == 1 :
        r += 31 - b 
        b = 0

print(r)

