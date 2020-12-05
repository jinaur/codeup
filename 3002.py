n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
r = -1

for i in range(0, m) :
    for j in range(0, n) :
        if a[j] == b[i] :
            r = j+1
            break
        
    print(r, end=" ")

