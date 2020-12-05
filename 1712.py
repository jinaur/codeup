a, b, k = list(map(int, input().split()))

count = b-a
for i in  range(a, k+1) :
    print(a, end=" ")
    if a+count > k :
        break
    a += count

