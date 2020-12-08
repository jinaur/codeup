a, b = list(map(int, input().split()))

count = 0
for i in range(a, b+1) :
    r = str(i)
    for j in range(0, len(r)) :
        if r[j] == '1' :
            count += 1

print(count)


