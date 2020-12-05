n, m = list(map(int, input().split()))

r = 1

for i in range(0, 7) :
    r = n * r
    if i <= 5 and r >= m :
        print("Dangerous")
        break
    if i >= 5 and r <= m :
        print("Safe")
        break

