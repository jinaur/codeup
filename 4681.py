a = list(map(int, input().split()))

r = 0

for i in range(0, len(a)) :
    r += a[i] ** 2

r = r % 10

print(r)
