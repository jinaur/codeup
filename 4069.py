n = int(input())

count = 0

for i in range(0, n) :
    if n == 1 :
        break

    if n % 5 == 0 :
        n = n // 5
        count += 1 
    elif n % 2 == 0 :
        n = n // 2
        count += 1
    else :
        n -= 1
        count += 1

print(count)