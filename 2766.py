n = int(input())

arr = []
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)

k = int(input())

def kill(x, y) :
    if x < 0 or y < 0 :
        return
    if x > n-1 or y > n-1 :
        return
    arr[x][y] = 0

for i in range(0, k) :
    x, y = list(map(int, input().split()))
    x = x-1
    y = y-1
    kill(x, y)
    kill(x-1, y)
    kill(x+1, y)
    kill(x, y-1)
    kill(x, y+1)
    kill(x-1, y-1)
    kill(x-1, y+1)
    kill(x+1, y-1)
    kill(x+1, y+1)

sum = 0
for line in arr :
    for v in line :
        sum += v

print(sum)

