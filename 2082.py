n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

for i in range(0, n) :
    if a[i] == k :
        print(i+1)
        exit()

print(-1)


