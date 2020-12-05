n = int(input())
m = int(input())
l = []
min = 10000000

count = 0
for i in range(n, m+1) :
    for j in range(n, i) :
        if i%j == 0 :
            l.append(i)
        if i < min :
            min = i

Sum = sum(l)
print(Sum)
print(min)