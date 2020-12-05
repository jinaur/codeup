n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

r = [0] * m

for i in range(0, n) :
    for j in range(0, m) :
        if a[i] == b[j] :
            r[j] = 1
            

r = ' '.join(map(str, r))
print(r)