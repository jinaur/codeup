n = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(0, n-1) :   
    if i == 0 and a[i] == 0 and a[i+1] == 0 :
        count += 1
        continue
    
    if a[i] == 0 and a[i+1] == 0 and a[i-1] == 0 :
        count += 1

    if i == n-2 and a[n-1] == 0 and a[n-2] == 0 :
        count += 1

if n == 1 and a[0] == 0 or n == 2 and a[0] == 0 and a[1] == 0 :
        count += 1

print(count)

