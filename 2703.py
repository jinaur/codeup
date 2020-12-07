n = int(input())
a = list(map(int, input().split()))

u_count = 0
d_count = 0

for i in range(1, n) :
    if a[i-1] < a[i] :
        u_count += 1
    elif a[i-1] > a[i] :
        d_count += 1

print(u_count, d_count)


