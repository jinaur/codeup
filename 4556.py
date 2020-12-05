n = int(input())
m = int(input())

r = 0
min = 100000

for i in range(n, m+1) :
    count = 0
    for j in range(n, i) :
        if i%j == 0 and i < min :
            min = i

        if i%j == 0 :
            r += i
        
        
print(r)
print(min)
