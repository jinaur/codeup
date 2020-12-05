n = int(input())
a = list(map(int, input().split()))
b = sorted(a)

for i in range(0, n) :
    for j in range(0, n) :
        if a[i] == b[j] :
            print(a[i], n-j)
            break

      
