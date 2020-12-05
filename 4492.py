n = int(input())

r = 0
for i in range(0, n) :
    a = list(map(int, input().split()))
    r += max(a)
    print(r)
    
print(r)