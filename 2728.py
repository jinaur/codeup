n = int(input())

r = 0
for i in range(0, n) :
    a = list(map(int, input().split()))
    Max = 0
    for j in range(0, i+1) :
        if a[j] > Max :
            Max = a[j]

    r += Max

print(r)