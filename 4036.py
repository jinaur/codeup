n = int(input())
m = int(input())

count = 0
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if i+j == n and abs(i-j) == m :
            print(j)
            print(i)
            count = 1
            break
    if count != 0 :
        break
