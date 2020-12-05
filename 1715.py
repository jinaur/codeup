a, b = list(map(int, input().split()))

for i in range(0, 10) :
    for j in range(2, b) :
        if a%j == 0 and b%j == 0 :
            a = a//j
            b = b//j

print(a, b)

