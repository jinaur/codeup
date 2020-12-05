a, b = list(map(int, input().split()))

r = 0
for i in range(a, b+1) :
    if i%3 == 0 :
        r += i 
    if i%4 == 0 :
        r -= i

print(r)

