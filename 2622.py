n = int(input())
a = list(map(int, input().split()))

Max = 0
Min = 100000000
for i in range(0, n) :
    if a[i] > Max :
        Max = a[i]
        Max_i = i+1
    if a[i] < Min :
        Min = a[i]
        Min_i = i+1

print(Max_i, ":", Max)
print(Min_i, ":", Min)

