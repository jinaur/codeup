n = int(input())
l = list(map(int, input().split()))
m = int(input())

for i in range(0, m) :
    a, b = list(map(int, input().split()))
    x = l[a-1:b]
    print(max(x), end=' ')

