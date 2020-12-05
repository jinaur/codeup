n = int(input())
a = list(map(int, input().split()))

max = 0
r = 0
for i in range(1, 5+1) :
    count = 0
    for j in range(0, n) :
        if a[j] == i :
            count += 1
        if count > max :
            max = i

print(max)
    