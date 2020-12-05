n = int(input())

a, b = 0, 0
for i in range(1, n) :
    if a != 0 or b != 0 :
        break
    for j in range(1, n) :
        if i*j == n :
            a = i
            b = j
            break

if a == 0 and b == 0 :
    print("wrong number")
else :
    print(a, b)

    