n = int(input())

count = 0
for i in range(0, n) :
    a, b = map(int, input().split())
    count += b % a
    

print(count)

