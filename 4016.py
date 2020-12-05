a, b, c = list(map(int, input().split()))

for i in range(100000, 0, -1) :
    if a%i == 0 and b%i == 0 and c%i == 0 :
        print(i)
        break

