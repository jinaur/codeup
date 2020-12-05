n = int(input())
a = list(map(int, input().split()))

Max = 0
Min = 1000
for i in range(0, n) :
    if a[i] > Max :
        Max = a[i]

for i in range(0, n) :
    if a[i] < Min :
        Min = a[i]

print(Max, Min)

