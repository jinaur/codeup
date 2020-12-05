# 5 
# 24 52
# 13 22
# 5 53
# 23 10
# 7 70
n = int(input())

count = 0
for i in range(0, n) :
    a, b = map(int, input().split())
    count += b % a
    

print(count)
