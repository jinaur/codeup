n = int(input())
a = list(map(int, input().split()))

l = [0]*23
for i in range(0, n) :
    l[a[i]-1] += 1

for i in range(0, 23) :
    print(l[i], end=" ")

