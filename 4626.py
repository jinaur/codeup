n = int(input())
l = list(map(int, input().split()))

x = 0
count = 0

for i in range(0, n) :
    if l[i] == 1 :
        count += 1
        x += count
    else :
        count = 0

print(x)
