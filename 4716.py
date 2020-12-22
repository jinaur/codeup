max = 0
MAX = 0

for i in range(0, 10) :
    a, b = list(map(int, input().split()))
    max -= a 
    max += b
    if max > MAX :
        MAX = max

print(MAX) 