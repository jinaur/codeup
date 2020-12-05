n = int(input())

count = 0

for i in range(0, n) :
    count += 1
    print(n-i, ":", "A->B")

for i in range(0, n) :
    count += 1
    print(n-i, ":", "B->C")

print(count)