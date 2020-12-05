n = int(input())
h = list(map(int, input().split()))

m = 1000
count = 0
r = h[0]

for i in range(0, n) :
    if h[i] < m and h[i] < 100 or m > h[i+1]:
        count += 1
    
    m = h[i]
    r = h[i]

print(count)