n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int,  input().split()))


for i in range(0, n) :
    for j in range(0, m) :
        if a[i] <= b[j] :
            print(n-i+1)
