n = int(input())
a = list(map(int, input().split()))

Max = 0
Min = 1000

for i in range(0, n) :
    if a[i] < Min :
        Min = a[i]
    elif a[i] > Max :
        Max = a[i]

r = Max-Min
print(r)
