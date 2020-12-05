n = int(input())
a = list(map(int, input().split()))

Min = 10000000000
for i in range(0, 5) :
    if abs(n-a[i]) < Min :
        Min = abs(n-a[i])

print(Min)

